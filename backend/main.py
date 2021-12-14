#!/usr/bin/python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import jwt
from hashlib import sha256
from json import loads
from time import time 
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import models

app = FastAPI()

origins = [
        "http://localhost:8000",
        "http://localhost:8080",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8080"
        ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
        )

# Init Database connection and await
class DBinit():
    def __init__(self , url:str):
        self.connect = AsyncIOMotorClient(url)
        self.database = self.connect["FCU_AWS"]
        asyncio.run_coroutine_threadsafe(self.init_connect() , asyncio.get_event_loop())

    async def init_connect(self):
        collections = await self.database.list_collections.names()
        for collect in ["users"]:
            if collect not in collections:
                await self.database.create_collection(collect)

    async def check_user(self , username:str , password:str=None) -> dict:
        return await self.database.find_one({
            "username" : username,
            "password" : sha256(password.encode()).hexdigest()
            })
            
    async def create_user(self , username:str , password:str) -> bool:
        if await self.get_user(username):
            return FileExistsError

        user = await self.database["username"].insert_one(
                {"username" : username , "password" : password , "locate" : None , "phone" : int}
                )
    
        return user

setting = {
        "user" : "mumu",
        "pass" : "mumu123123123",
        "ip" : "114.33.1.57",
        "port" : "27000"
        }

db = DBinit("mongodb://{user}:{pass}@{ip}:{port}".format(**setting))

@app.post("/login" , response_model=models.ReponseLogin)
async def login(username:str , password:str):
    db = loads(open("db.json" , "rb").read())

    password = sha256(password).hexdigest()
    res = await db.check_user(username , password)
    if(not res):
        return False

    loginTime = int(time.time())
    expiredTime = loginTime + 10 * 60 # add 10 minutes 
    payload = ({
            "loginTime" : loginTime ,
            "expiredTime" : expiredTime ,
            "username" : username
            })
    
    return jwt.encode(payload , key="FCU_AWS" , algorithm="HS256")

@app.get("/register" , response_model=PostRegister)
def register(data:models.PostRegister):
    
    try:
        user = await db.create_user(**data)
    except FileExistsError:
        return HTTPException(409 , "User already exists.")
   
    return {
        "status" : 200,
        "payload" : jwt.encode({
            "username" : user},
            key="FCU_AWS",
            algorithm="HS256"
            )
        }

