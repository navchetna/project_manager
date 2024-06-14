from fastapi import APIRouter
from prisma import Prisma
from server.schemas import CollegeCreate, CollegeRead

router = APIRouter()
prisma = Prisma()

@router.post('/colleges', response_model=CollegeRead)
async def create_college(college: CollegeCreate):
    college = await prisma.college.create(data=college.dict())
    return college

@router.get('/colleges/{college_id}', response_model=CollegeRead)
async def read_college(college_id: int):
    college = await prisma.college.find_unique(
        where={'college_id': college_id},
    )
    return college
