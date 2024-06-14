from pydantic import BaseModel, EmailStr

class MentorCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    enterprise_id: int

class MentorRead(MentorCreate):
    mentor_id: int

    class Config:
        orm_mode = True
