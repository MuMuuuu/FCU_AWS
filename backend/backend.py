#!/usr/bin/python3

from flask import request
import jwt
from hashlib import sha256
from json import loads

app = Flask(__name__)

@app.route("/login" , method=["POST"])
def login():
    # connect to MongoDB
    db = loads(open("db.json" , "rb").read())
    data = request.json
    username = data["username"]
    password = sha256(data["password"]).hexdigest()
    if sha256(db[username]).hexdigest() == password:
        


