from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from dependecies import get_prisma
from schemas.project import ProjectCreate, ProjectRead

router = APIRouter()
prisma = Prisma()

@router.post('/projects', response_model=ProjectRead)
async def create_project(project: ProjectCreate, prisma: Prisma = Depends(get_prisma)):
    project = await prisma.project.create(data=project.dict())
    return project

@router.get('/projects/{project_id}', response_model=ProjectRead)
async def read_project(project_id: int, prisma: Prisma = Depends(get_prisma)):
    project = await prisma.project.find_unique(
        where={'project_id': project_id},
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.get('/projects', response_model=list[ProjectRead])
async def read_projects(skip: int = 0, take: int = 10, prisma: Prisma = Depends(get_prisma)):
    projects = await prisma.project.find_many(skip=skip, take=take)
    return projects
