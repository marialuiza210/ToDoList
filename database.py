import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("MONGO_INITDB_ROOT_USERNAME")
password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

MONGO_URL = f"mongodb://{username}:{password}@localhost:27018"

client = AsyncIOMotorClient(MONGO_URL)