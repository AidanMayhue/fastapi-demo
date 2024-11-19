#!/usr/bin/env python3


from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os
import pandas as pd
import mysql.connector



DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "xdw9vp"



db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/square/{a}/")
def square(a: int):
    return {"square": a * a}

@app.get('/genres', methods=['GET'], cors=True)
def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        output = json.dumps(json_data)
        return(output)
    except mysql.connector.Error as e:
        print("MySQL Error: ", str(e))
        return None
    cur.close()

@app.get('/songs', methods=['GET'], cors=True)
def get_songs():
    query = "SELECT songs.title, songs.album, songs.artist, songs.year, songs.file, songs.image, genres.genre FROM songs JOIN genres ON songs.genre=genres.genreid ORDER BY songs.title ASC;" 
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        output = json.dumps(json_data)
        return(output)
    except mysql.connector.Error as e:
        print("MySQL Error: ", str(e))
        return None
    cur.close()
