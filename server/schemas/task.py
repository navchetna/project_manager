from pydantic import BaseModel

class TaskCreate(BaseModel):
    description: str
    completed: bool
    project_id: int

class TaskRead(TaskCreate):
    task_id: int

    class Config:
        orm_mode = True
