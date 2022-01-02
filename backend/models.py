#!/usr/bin/python3

from typing import Optional, Union, List
from pydantic import BaseModel

class BasicResponse(BaseModel):
    status: int

class PostLogin(BaseModel):
    username: str
    password: str

class ResponseLogin(BasicResponse):
    token: str = None


class PostRegister(PostLogin):
    phone: int


class PostLocation(BaseModel):
    store: str


class Location(BaseModel):
    store: str
    timestamp: int


class StoreLocation(Location):
    username: str


class ResponseProfile(BaseModel):
    username: str
    locations: List[Location] = []


class ResponseStoreHistory(BaseModel):
    locations: List[StoreLocation] = []
