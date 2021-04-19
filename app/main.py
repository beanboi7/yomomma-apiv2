#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from typing import Optional
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import json

with open('./jokes.json') as f:
  all_jokes = json.load(f)
no_of_jokes = len(all_jokes)

app = FastAPI()

@app.get("/")
async def home():
    return {"joke": "Yo mama"}

@app.get("/jokes")
async def send_joke(fmt: Optional[str] = None, count: Optional[int] = 1):
  if fmt:
    if count > 1 and count < no_of_jokes:
      return [random.choice(all_jokes) for i in range(count)]
    elif count == 1:
       return random.choice(all_jokes)
    else:
      raise HTTPException(status_code=404, detail="Invalid count paramter")
  
  if count > 1 and count < no_of_jokes:
    return [{"joke": random.choice(all_jokes)} for i in range(count)]
  elif count == 1:
    return {"joke": random.choice(all_jokes)}
  else:
    raise HTTPException(status_code=404, detail="Invalid count paramter")

@app.get("/jokes/{index}")
async def send_specific_joke(index: int):
    if index>no_of_jokes:
      raise HTTPException(status_code=404, detail="Index out of range")
    return {"joke": all_jokes[index]}