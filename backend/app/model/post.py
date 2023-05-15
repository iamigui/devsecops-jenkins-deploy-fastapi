from pydantic import BaseModel, Field
from typing import List, Optional
from app.model.types import PyObjectId
from datetime import datetime
from bson import ObjectId

class Post(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    author: str
    title: str
    content: str
    created_at: datetime
    refs_links: List[str]

    class Config:
        json_encoders = {ObjectId: str}

class NewPost(BaseModel):
    author: str
    title: str
    content: str
    refs_links: List[str]

    class Config:
        json_encoders = {ObjectId: str}

class EditPost(BaseModel):
    author: Optional[str]
    title: Optional[str]
    content: Optional[str]
    refs_links: Optional[List[str]]

    class Config:
        json_encoders = {ObjectId: str}