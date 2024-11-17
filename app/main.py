#!/usr/bin/env python3
<<<<<<< HEAD

from fastapi import FastAPI ,Request
=======
import mysql.connector
from fastapi import FastAPI
>>>>>>> db26ff669f9c2b5471f6a4c107ecf185285a1d79
from typing import Optional
from pydantic import BaseModel
import json
import os
import pandas as pd
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

<<<<<<< HEAD
@app.get("/customer/{idx}")
def customer(idx: int):
    df = pd.read_csv("../customers.csv")
    customer = df.iloc[idx]
    return customer.to_dict()


@app.post("/get_body")
async def get_body(request: Request):
    response = await request.json()
    first_name = response["fname"]
    last_name = response["lname"]
    favorite_number = response["favnu"]
    return {"first_name": first_name, "last_name": last_name, "favorite_number": favorite_number}

=======
>>>>>>> db26ff669f9c2b5471f6a4c107ecf185285a1d79
@app.route('/genres', methods=['GET'], cors=True)
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
