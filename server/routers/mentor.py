from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from utils.dependencies import get_prisma
from schemas.mentor import MentorCreate, MentorRead

router = APIRouter()
prisma = Prisma()

@router.post('/mentors', response_model=MentorRead)
async def create_mentor(mentor: MentorCreate, prisma: Prisma = Depends(get_prisma)):
    mentor = await prisma.mentor.create(data=mentor.dict())
    return mentor

@router.get('/mentors/{mentor_id}', response_model=MentorRead)
async def read_mentor(mentor_id: int, prisma: Prisma = Depends(get_prisma)):
    mentor = await prisma.mentor.find_unique(
        where={'mentor_id': mentor_id},
    )
    if not mentor:
        raise HTTPException(status_code=404, detail="Mentor not found")
    return mentor

@router.get('/mentors', response_model=list[MentorRead])
async def read_mentor(skip: int = 0, take: int = 10, prisma: Prisma = Depends(get_prisma)):
    mentor = await prisma.mentor.find_many(skip=skip, take=take)
    return mentor