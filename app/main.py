#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
from typing import Optional
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from json import load

from starlette.requests import Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

with open('./jokes.json') as f:
    all_jokes = load(f)

limiter = Limiter(key_func=get_remote_address, default_limits = ["5/minute"])
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

@app.get("/")
async def home():
    return {"joke": "Yo momma"}


@app.get("/jokes")
async def send_joke(count: Optional[int] = 1):
    if count > 1 and count < len(all_jokes):
        return [{"joke": choice(all_jokes)} for i in range(count)]
    elif count == 1:
        return {"joke": choice(all_jokes)}
    else:
        raise HTTPException(status_code=404, detail="Invalid count parameter")


@app.get("/jokes/{index}")
async def send_specific_joke(index: int):
    if index > len(all_jokes) or index < 0:
        raise HTTPException(status_code=404, detail="Index out of range")
    return {"joke": all_jokes[index]}


@app.get("/search")
async def search_joke(query: str):
    if query.lower() == "yo momma":
        return {"results": "DON'T"}

    result = [joke for joke in all_jokes if query in joke.lower().split()]
    return {"results": result}
