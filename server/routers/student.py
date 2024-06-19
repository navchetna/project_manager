from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from utils.dependencies import get_prisma
from schemas.student import StudentCreate, StudentRead

router = APIRouter()
prisma = Prisma()

@router.post('/students', response_model=StudentRead)
async def create_student(student: StudentCreate, prisma: Prisma = Depends(get_prisma)):
    student = await prisma.student.create(data=student.dict())
    return student

@router.get('/students/{student_id}', response_model=StudentRead)
async def read_student(student_id: int, prisma: Prisma = Depends(get_prisma)):
    student = await prisma.student.find_unique(
        where={'student_id': student_id},
    )
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get('/students', response_model=list[StudentRead])
async def read_students(skip: int = 0, take: int = 10, prisma: Prisma = Depends(get_prisma)):
    students = await prisma.student.find_many(skip=skip, take=take)
    return students
