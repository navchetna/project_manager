from fastapi import APIRouter
from prisma import Prisma
from server.schemas.task import TaskCreate, TaskRead

router = APIRouter()
prisma = Prisma()

@router.post('/tasks', response_model=TaskRead)
async def create_task(task: TaskCreate):
    task = await prisma.task.create(data=task.dict())
    return task

@router.get('/tasks/{task_id}', response_model=TaskRead)
async def read_task(task_id: int):
    task = await prisma.task.find_unique(
        where={'task_id': task_id},
    )
    return task

@router.get('/tasks', response_model=list[TaskRead])
async def read_tasks(skip: int = 0, take: int = 10):
    tasks = await prisma.task.find_many(skip=skip, take=take)
    return tasks
