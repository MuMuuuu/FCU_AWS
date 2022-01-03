from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from hashlib import sha256
from time import time
from config import *

# Init Database connection and await
class Database:
    def __init__(self, url: str):
        self.connect = AsyncIOMotorClient(url)
        self.database = self.connect["FCU_AWS"]
        asyncio.run_coroutine_threadsafe(self.init_connect(), asyncio.get_event_loop())

    async def init_connect(self):
        collections = await self.database.list_collections.names()
        for collect in ["users"]:
            if collect not in collections:
                await self.database.create_collection(collect)

    async def get_user(self, username: str, password: str = None) -> dict:
        query = {"username": username}
        if password:
            query["password"] = sha256(password.encode()).hexdigest()

        return await self.database["users"].find_one(query)

    async def create_user(self, username: str, password: str, phone: int):
        if await self.get_user(username):
            return FileExistsError

        password_hash = sha256(password.encode()).hexdigest()
        await self.database["users"].insert_one(
            {"username": username, "password": password_hash, "phone": phone, "type": "user"}
        )

    async def update_user_location(self, username: str, store: str):
        current_time = int(time())
        await self.database["users"].update_one(
            {"username": username}, {"$push": {"locations": {"store": store, "timestamp": current_time}}}
        )

    async def get_store_locations(self, store: str) -> list:
        async for clan in self.database["users"].aggregate(
            [
                {"$unwind": "$locations"},
                {"$match": {"locations.store": store}},
                {"$addFields": {"locations.username": "$username"}},
                {"$group": {"_id": None, "locations": {"$push": "$locations"}}},
            ]
        ):
            data = clan.get("locations")
            data.sort(key=lambda x: x["timestamp"], reverse=True)
            return data

        return []
