#!/usr/bin/python3
/
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import jwt
from hashlib import sha256
import json
from time import time 
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import models
from config import *
import qrcode
from io import BytesIO
from base64 import b64encode as b64e

app = FastAPI()

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

db = DBinit("mongodb://{user}:{pass}@{ip}:{port}".format(**mongo_setting))

@app.post("/login" , response_model=models.ReponseLogin)
async def login(username:str , password:str):
    db = json.loads(open("db.json" , "rb").read())

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
    
    return jwt.encode(payload , key=JWT_KEY , algorithm=JWT_ALG)

@app.get("/register" , response_model=PostRegister)
def register(data:models.PostRegister):
    
    try:
        user = await db.create_user(**data)
    except FileExistsError:
        return HTTPException(409 , "User already exists.")
   
    return {
        "status" : 200,
        "payload" : jwt.encode(
            {"username" : user},
            key=JWT_KEY,
            algorithm=JWT_ALG
            )
        }

@app.get("/{store}/qrcode")
def qrcode_gen(store:str):
    qr = qrcode.QR(
            border=6,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=3,
            mask_pattern=5,
            )
    buffer = BytesIO()
    
    qr.add_data(json.dumps({"store_name" : store}))
    qr.make(fit=True)
    img = qr.make_image()
    img.save(buffer)

    qrbase = b64e(buffer.getvalue()).decode()    

    return "data:image/png:base64,{}".format(qrbase) 

