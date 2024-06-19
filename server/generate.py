import os

# Templates for the generated code
ROUTER_TEMPLATE = '''from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from utils.dependencies import get_prisma
from schemas.{object_name_snake} import {object_name_pascal}Create, {object_name_pascal}Read

router = APIRouter()
prisma = Prisma()

@router.post('/{object_name_plural}', response_model={object_name_pascal}Read)
async def create_{object_name_snake}({object_name_snake}: {object_name_pascal}Create, prisma: Prisma = Depends(get_prisma)):
    {object_name_snake} = await prisma.{object_name_snake}.create(data={object_name_snake}.dict())
    return {object_name_snake}

@router.get('/{object_name_plural}/{{{object_name_snake}_id}}', response_model={object_name_pascal}Read)
async def read_{object_name_snake}({object_name_snake}_id: int, prisma: Prisma = Depends(get_prisma)):
    {object_name_snake} = await prisma.{object_name_snake}.find_unique(
        where={{'{object_name_snake}_id': {object_name_snake}_id}},
    )
    if not {object_name_snake}:
        raise HTTPException(status_code=404, detail="{object_name_pascal} not found")
    return {object_name_snake}

@router.get('/{object_name_plural}', response_model=list[{object_name_pascal}Read])
async def read_{object_name_plural}(skip: int = 0, take: int = 10, prisma: Prisma = Depends(get_prisma)):
    {object_name_plural} = await prisma.{object_name_snake}.find_many(skip=skip, take=take)
    return {object_name_plural}
'''

SCHEMA_TEMPLATE = '''from pydantic import BaseModel

class {object_name_pascal}Create(BaseModel):
    {fields}

class {object_name_pascal}Read({object_name_pascal}Create):
    {object_name_snake}_id: int

    class Config:
        orm_mode = True
'''

def generate_code(object_schema: str):
    # Parse the input schema to get the object name and fields
    lines = object_schema.strip().splitlines()
    object_name = lines[0].split()[1]
    fields = lines[1:-1]
    
    object_name_snake = object_name.lower()
    object_name_pascal = object_name.capitalize()
    object_name_plural = object_name_snake + 's'
    
    # Generate the fields for the schema file
    fields_str = "\n    ".join([f"{field.split()[0]}: {map_prisma_to_python(field.split()[1])}" for field in fields if '[]' not in field])
    
    # Create the router and schema code using the templates
    router_code = ROUTER_TEMPLATE.format(
        object_name_snake=object_name_snake,
        object_name_pascal=object_name_pascal,
        object_name_plural=object_name_plural,
    )
    
    schema_code = SCHEMA_TEMPLATE.format(
        object_name_snake=object_name_snake,
        object_name_pascal=object_name_pascal,
        fields=fields_str,
    )
    
    # Write the generated code to the respective files
    write_to_file(f'server/routers/{object_name_snake}.py', router_code)
    write_to_file(f'server/schemas/{object_name_snake}.py', schema_code)

def map_prisma_to_python(prisma_type: str) -> str:
    # Map Prisma types to Python types for Pydantic
    mapping = {
        'String': 'str',
        'BigInt': 'int',
        'Int': 'int',
        'Boolean': 'bool',
        'Float': 'float',
        'DateTime': 'datetime.datetime',
    }
    return mapping.get(prisma_type, 'Any')

def write_to_file(filepath: str, content: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as file:
        file.write(content)

# Example usage
new_schema = '''model testModel {
  enterprise_id   BigInt  @id @default(autoincrement())
  enterprise_name String
  industry        String
  mentors         Mentor[]
}'''

generate_code(new_schema)
