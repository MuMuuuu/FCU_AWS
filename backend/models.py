#!/usr/bin/python3

from typing import Optional, Union, List
from pydantic import BaseModel

class PostLogin(BaseModel):
    username: str
    password: str


class ResponseLogin(BaseModel):
    status: int
    token: str = None


class PostRegister(PostLogin):
    phone: str


class Verify(BaseModel):
    jwt : str 


class ReportLocation(Verify):
    location:str


class ResponseProfile(PostLogin):
    location: str
    phone : str


class ResponseList(BaseModel):
    uesrname : str


