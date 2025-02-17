import os
from motor.motor_asyncio import AsyncIOMotorClient

DB_URL = os.getenv("DB_URI")
client = AsyncIOMotorClient(DB_URL)

db = client["CookBook"]
recipes_collection = db["recipes_collection"]
