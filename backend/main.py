#!/usr/bin/python3

from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import jwt
from hashlib import sha256
import json
from time import time
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import models
from config import *
from store import store

app = FastAPI()

app.include_router(store.router)

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)


# Init Database connection and await
class DBinit:
    def __init__(self, url: str):
        self.connect = AsyncIOMotorClient(url)
        self.database = self.connect["FCU_AWS"]
        asyncio.run_coroutine_threadsafe(self.init_connect(), asyncio.get_event_loop())

    async def init_connect(self):
        collections = await self.database.list_collections.names()
        for collect in ["users"]:
            if collect not in collections:
                await self.database.create_collection(collect)

    async def check_user(self, username: str, password: str = None) -> dict:
        query = {"username": username}
        if password:
            query["password"] = sha256(password.encode()).hexdigest()

        return await self.database["users"].find_one(query)

    async def create_user(self, username: str, password: str, phone: int) -> dict:
        if await self.check_user(username):
            return FileExistsError

        password_hash = sha256(password.encode()).hexdigest()
        user = await self.database["users"].insert_one(
            {"username": username, "password": password_hash, "phone": phone}
        )

        return user

    async def return_location(self, username):
        return await self.database["users"].find_one({"username": username})

    async def update_location(self, username, location):
        await self.database["users"].update_one({"username": username}, {"location": location})


db = DBinit("mongodb://{user}:{pass}@{ip}:{port}".format(**MONGO_SETTINGS))


@app.post("/login", response_model=models.ResponseLogin)
async def login(data: models.PostLogin):
    user = await db.check_user(**data.dict())
    if not user:
        return {"status": 404}

    loginTime = int(time())
    expiredTime = loginTime + 10 * 60  # add 10 minutes
    payload = {"loginTime": loginTime, "expiredTime": expiredTime, "username": user["username"]}

    return {"status": 200, "token": jwt.encode(payload, key=JWT_KEY, algorithm=JWT_ALG)}


@app.post("/register", response_model=models.ResponseLogin)
async def register(data: models.PostRegister):
    try:
        await db.create_user(**data.dict())
    except FileExistsError:
        return HTTPException(409, "User already exists.")

    return {"status": 200, "payload": jwt.encode({"username": data.username}, key=JWT_KEY, algorithm=JWT_ALG)}


@app.get("/report/{store}", response_model=models.ReportLocation)
async def report(data: models.ReportLocation):
    try:
        result = jwt.decode(data["jwt"], KEY=JWT_KEY, algorithm=JWT_ALG)
    except jwt.DecodeError:
        return HTTPException(403 , "JWT DecodeError")

    await db.update_location(result["username"], result["location"])


@app.get("/profile" , response_model=models.Verify)
async def profile(username):
    try:
        result = jwt.decode(data["jwt"], KEY=JWT_KEY, algorithm=JWT_ALG)
    except jwt.DecodeError:
        return HTTPException(403 , "JWT DecodeError")
    
    return await db.find_one({"users" : username})

