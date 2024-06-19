from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers import college, enterprise, mentor, project, student, task
from utils.includeRouters import include_all_routers

import os
from dotenv import load_dotenv
import asyncio
from prisma import Prisma

app = FastAPI()

prisma = Prisma()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

# Dynamically include all routers from the routers directory
include_all_routers(app, 'routers')