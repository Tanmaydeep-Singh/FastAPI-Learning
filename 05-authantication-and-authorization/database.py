from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB Atlas Connection
client = AsyncIOMotorClient("mongodb+srv://Tanmaydeep:tanmay@cluster1.vcm3w.mongodb.net/FASTAPI-CONNECTION")

database = client.storyloom
print("DATABASE", database)

collection = database.get_collection("users")
