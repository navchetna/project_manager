from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from utils.dependencies import get_prisma
from schemas.college import CollegeCreate, CollegeRead

router = APIRouter()
prisma = Prisma()

@router.post('/colleges', response_model=CollegeRead)
async def create_college(college: CollegeCreate, prisma: Prisma = Depends(get_prisma)):
    college = await prisma.college.create(data=college.dict())
    return college

@router.get('/colleges/{college_id}', response_model=CollegeRead)
async def read_college(college_id: int, prisma: Prisma = Depends(get_prisma)):
    college = await prisma.college.find_unique(
        where={'college_id': college_id},
    )
    if not college:
        raise HTTPException(status_code=404, detail="College not found")
    return college

@router.get('/colleges', response_model=list[CollegeRead])
async def read_colleges(skip: int = 0, take: int = 10, prisma: Prisma = Depends(get_prisma)):
    colleges = await prisma.college.find_many(skip=skip, take=take)
    return colleges