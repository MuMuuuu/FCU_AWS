#!/usr/bin/python3

from pydantic import BaseModel

class PostLogin(BaseModel):
    username : str
    password : str

class ResponseLogin(BaseModel):
    status : int
    token : str=None

class PostRegister(BaseModel):
    phone : str
    username : str
    password : str
    check_password : str

class ReportLocation(BaseModel):
    jwt : str 
    locate : str

