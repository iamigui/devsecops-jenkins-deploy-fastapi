from motor.motor_asyncio import AsyncIOMotorCollection
from app.model.post import Post, NewPost, EditPost
from typing import List, Dict
from datetime import datetime, timedelta
from fastapi import HTTPException
from app.model.types import PyObjectId
from pymongo import ReturnDocument


class AppService:
    collection: AsyncIOMotorCollection

    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def get_posts(self) -> List[Post]:
        res = self.collection.find()

        return [Post(**post) async for post in res]
    
    async def get_post(self, id: PyObjectId) -> Post:
        res = await self.collection.find_one({"_id": id})

        print(res)

        if res:
            return Post(
                id = res["_id"],
                **res
            )
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    
    async def create_post(self, post: NewPost) -> Post:
        newPost = post.dict()
        newPost["created_at"] = datetime.now() + timedelta(hours=2)
        res = await self.collection.insert_one(newPost)

        if res:
            return Post(
                id=res.inserted_id,
                **newPost)
        
    async def delete_post(self, id: PyObjectId) -> Dict:
        res = await self.collection.delete_one(
            {"_id": id}
        )

        if res.deleted_count == 1:
            return {
                "message": "Post deleted successfully"
            }
        else:
            raise HTTPException(status_code=404, detail="Post not found")
        
    async def modify_post(self, id: PyObjectId, post: EditPost) -> Post:
        # Modify and return the modified document
        result = await self.collection.find_one_and_update(
            {"_id": id},
            {"$set": {k: v for k ,v in post.dict().items() if v is not None}},
            return_document=ReturnDocument.AFTER
        )

        if result:
            return Post(
                id = result["_id"],
                **result
            )
        else:
            raise HTTPException(status_code=404, detail="Post not found")