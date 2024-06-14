from fastapi import APIRouter
from prisma import Prisma
from server.schemas.student import StudentCreate, StudentRead

router = APIRouter()
prisma = Prisma()

@router.post('/students', response_model=StudentRead)
async def create_student(student: StudentCreate):
    student = await prisma.student.create(data=student.dict())
    return student

@router.get('/students/{student_id}', response_model=StudentRead)
async def read_student(student_id: int):
    student = await prisma.student.find_unique(
        where={'student_id': student_id},
    )
    return student

@router.get('/students', response_model=list[StudentRead])
async def read_students(skip: int = 0, take: int = 10):
    students = await prisma.student.find_many(skip=skip, take=take)
    return students
