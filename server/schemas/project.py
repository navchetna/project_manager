from pydantic import BaseModel

class ProjectCreate(BaseModel):
    project_name: str
    description: str
    category: str
    mentor_id: int

class ProjectRead(ProjectCreate):
    project_id: int

    class Config:
        orm_mode = True
