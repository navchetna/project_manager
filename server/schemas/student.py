from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    usn: str
    department: str
    project_id: int
    college_id: int

class StudentRead(StudentCreate):
    student_id: int

    class Config:
        orm_mode = True
