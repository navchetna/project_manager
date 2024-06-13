import asyncio
from prisma import Prisma
from prisma.models import User

class writeDataClass:
    async def main(self) -> bool:
        db = Prisma(auto_register=True)
        print("Before connecting to db")
        await db.connect()
        print("After connecting to db")

        # write your queries here
        try:
            user = await db.user.create_many(
                data=
                [
                    {
                        'grade': 5,
                        'name': "Faiz Feroz",
                        'city': "Houston",
                    },
                    {
                        'grade': 6,
                        'name': "Darren Nishan Patrao",
                        'city': "Toronto",
                    },
                ]
            )
            await db.disconnect()
            return True
        except:
            print("An error occurred while writing to the DB")
            await db.disconnect()
            return False

if __name__ == '__main__':
    write_data_instance = writeDataClass()
    asyncio.run(write_data_instance.main())