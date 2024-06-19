from prisma import Prisma

prisma = Prisma()

async def get_prisma() -> Prisma:
    if not prisma.is_connected():
        await prisma.connect()
    return prisma