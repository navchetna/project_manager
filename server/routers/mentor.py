from fastapi import APIRouter
from prisma import Prisma
from server.schemas.mentor import MentorCreate, MentorRead

router = APIRouter()
prisma = Prisma()

@router.post('/mentors', response_model=MentorRead)
async def create_mentor(mentor: MentorCreate):
    mentor = await prisma.mentor.create(data=mentor.dict())
    return mentor

@router.get('/mentors/{mentor_id}', response_model=MentorRead)
async def read_mentor(mentor_id: int):
    mentor = await prisma.mentor.find_unique(
        where={'mentor_id': mentor_id},
    )
    return mentor
