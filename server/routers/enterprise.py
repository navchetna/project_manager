from fastapi import APIRouter
from prisma import Prisma
from server.schemas.enterprise import EnterpriseCreate, EnterpriseRead

router = APIRouter()
prisma = Prisma()

@router.post('/enterprises', response_model=EnterpriseRead)
async def create_enterprise(enterprise: EnterpriseCreate):
    enterprise = await prisma.enterprise.create(data=enterprise.dict())
    return enterprise

@router.get('/enterprises/{enterprise_id}', response_model=EnterpriseRead)
async def read_enterprise(enterprise_id: int):
    enterprise = await prisma.enterprise.find_unique(
        where={'enterprise_id': enterprise_id},
    )
    return enterprise