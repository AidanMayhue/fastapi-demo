#!/usr/bin/env python3
import mysql.connector
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os
#a
#aaaaa
app = FastAPI()

DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "xdw9vp"

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/square/{a}/")
def square(a: int):
    return {"square": a * a}
