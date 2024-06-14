from pydantic import BaseModel

class CollegeCreate(BaseModel):
    college_name: str
    location: str

class CollegeRead(CollegeCreate):
    college_id: int

    class Config:
        orm_mode = True
