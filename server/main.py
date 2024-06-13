from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

@app.get('/')
def read_root():
    return {"DB_URL": DATABASE_URL}

@app.get('/access')
def read_root():
    return {"DB_URL": DATABASE_URL}