#!/usr/bin/python3

from flask import Flask
import jwt

app = Flask(__name__)

@app.route("/")
def login():
    

