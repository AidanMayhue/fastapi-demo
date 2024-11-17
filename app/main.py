#!/usr/bin/env python3

from fastapi import FastAPI ,Request
from typing import Optional
from pydantic import BaseModel
import json
import os
import pandas as pd
#a
#aaaaa
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
