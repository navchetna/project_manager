from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from dependecies import get_prisma
from schemas.task import TaskCreate, TaskRead

router = APIRouter()
prisma = Prisma()

@router.post('/tasks', response_model=TaskRead)
async def create_task(task: TaskCreate, prisma: Prisma = Depends(get_prisma)):
    task = await prisma.task.create(data=task.dict())
    return task

@router.get('/tasks/{task_id}', response_model=TaskRead)
async def read_task(task_id: int, prisma: Prisma = Depends(get_prisma)):
    task = await prisma.task.find_unique(
        where={'task_id': task_id},
    )
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get('/tasks', response_model=list[TaskRead])
async def read_tasks(skip: int = 0, take: int = 10, prisma: Prisma = Depends(get_prisma)):
    tasks = await prisma.task.find_many(skip=skip, take=take)
    return tasks
