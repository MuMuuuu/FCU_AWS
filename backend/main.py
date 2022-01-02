#!/usr/bin/python3

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import Depends
import jwt
from time import time
import models
from config import *
import auth
from auth import LoginState
from database import Database

app = FastAPI()
db = Database("mongodb://{user}:{pass}@{ip}:{port}".format(**MONGO_SETTINGS))

from store import store
app.include_router(store.router)

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)


@app.post("/login", response_model=models.ResponseLogin)
async def login(data: models.PostLogin):
    user = await db.get_user(**data.dict())
    if not user:
        return {"status": 404}

    loginTime = int(time())
    expiredTime = loginTime + 60 * 60  # add 10 minutes
    payload = {"iat": loginTime, "exp": expiredTime, "username": user["username"], "type": user["type"]}

    return {"status": 200, "token": jwt.encode(payload, key=JWT_KEY, algorithm=JWT_ALG)}


@app.post("/register", response_model=models.ResponseLogin)
async def register(data: models.PostRegister):
    try:
        await db.create_user(**data.dict())
    except FileExistsError:
        return HTTPException(409, "User already exists.")

    login_time = int(time())
    expired_time = login_time + 60 * 60  # add 10 minutes
    payload = {"iat": login_time, "exp": expired_time, "username": data.username, "type": "user"}

    return {"status": 200, "payload": jwt.encode(payload, key=JWT_KEY, algorithm=JWT_ALG)}


@app.get("/profile", response_model=models.ResponseProfile)
async def profile(login_state: LoginState = Depends(auth.get_login_state)):
    return await db.get_user(username=login_state.username)
