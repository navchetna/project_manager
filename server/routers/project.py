from fastapi import APIRouter
from prisma import Prisma
from server.schemas.project import ProjectCreate, ProjectRead

router = APIRouter()
prisma = Prisma()

@router.post('/projects', response_model=ProjectRead)
async def create_project(project: ProjectCreate):
    project = await prisma.project.create(data=project.dict())
    return project

@router.get('/projects/{project_id}', response_model=ProjectRead)
async def read_project(project_id: int):
    project = await prisma.project.find_unique(
        where={'project_id': project_id},
    )
    return project

@router.get('/projects', response_model=list[ProjectRead])
async def read_projects(skip: int = 0, take: int = 10):
    projects = await prisma.project.find_many(skip=skip, take=take)
    return projects
