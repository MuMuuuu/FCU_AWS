#!/usr/bin/python3

from typing import Optional, Union
from pydantic import BaseModel


class PostLogin(BaseModel):
    username: str
    password: str


class ResponseLogin(BaseModel):
    status: int
    token: str = None


class PostRegister(PostLogin):
    phone: int


class ReportLocation(BaseModel):
    jwt:str
    location:str
