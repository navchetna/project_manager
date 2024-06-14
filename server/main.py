from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from server.routers import college, enterprise, mentor, project, student, task

import os
from dotenv import load_dotenv
import asyncio
from prisma import Prisma

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

app.include_router(college.router)
app.include_router(enterprise.router)
app.include_router(mentor.router)
app.include_router(project.router)
app.include_router(student.router)
app.include_router(task.router)

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()