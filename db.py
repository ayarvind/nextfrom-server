import os
from motor.motor_asyncio import AsyncIOMotorClient
from config import DATABASE_NAME

uri = os.environ.get('MONGO_URI')
print(uri)
if not uri:
    raise Exception('MONGO_URI not found')

client = AsyncIOMotorClient(uri)
db = client[DATABASE_NAME]


