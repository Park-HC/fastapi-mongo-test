import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.garak_test

article_collection = database.get_collection("test")

def article_helper(article) -> dict:
    return {
        "id": str(article["_id"]),
        "title": article["title"],
        "content": article["content"],
        # "files": article["files"],
    }

async def retrieve_articles():
    articles = []
    async for article in article_collection.find():
        articles.append(article_helper(article))
    return articles

async def retrieve_article(id: str) -> dict:
    article = await article_collection.find_one({"_id": ObjectId(id)})
    if article:
        return article_helper(article)

async def add_article(article_data: dict) -> dict:
    article = await article_collection.insert_one(article_data)
    new_article = await article_collection.find_one({"_id": article.inserted_id})
    return article_helper(new_article)

async def update_article(id: str, data: dict):
    if len(data) < 1:
        return False
    article = await article_collection.find_one({"_id": ObjectId(id)})
    if article:
        updated_article = await article_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_article:
            return True
        return False

async def delete_article(id: str):
    article = await article_collection.find_one({"_id", ObjectId(id)})
    if article:
        await article_collection.delete_one({"_id": ObjectId(id)})
        return True
