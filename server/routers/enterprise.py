from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from dependecies import get_prisma
from schemas.enterprise import EnterpriseCreate, EnterpriseRead

router = APIRouter()
prisma = Prisma()

@router.post('/enterprises', response_model=EnterpriseRead)
async def create_enterprise(enterprise: EnterpriseCreate, prisma: Prisma = Depends(get_prisma)):
    enterprise = await prisma.enterprise.create(data=enterprise.dict())
    return enterprise

@router.get('/enterprises/{enterprise_id}', response_model=EnterpriseRead)
async def read_enterprise(enterprise_id: int, prisma: Prisma = Depends(get_prisma)):
    enterprise = await prisma.enterprise.find_unique(
        where={'enterprise_id': enterprise_id},
    )
    if not enterprise:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    return enterprise

@router.get('/enterprises', response_model=list[EnterpriseRead])
async def read_enterprises(skip: int = 0, take: int = 10, prisma: Prisma = Depends(get_prisma)):
    enterprises = await prisma.enterprise.find_many(skip=skip, take=take)
    return enterprises