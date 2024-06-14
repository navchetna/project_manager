from pydantic import BaseModel

class EnterpriseCreate(BaseModel):
    enterprise_name: str
    industry: str

class EnterpriseRead(EnterpriseCreate):
    enterprise_id: int

    class Config:
        orm_mode = True