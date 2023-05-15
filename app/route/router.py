from fastapi import APIRouter, Depends
from app.dependencies import get_app_service
from app.model.post import Post, NewPost, EditPost
from typing import List
from app.model.types import PyObjectId

router = APIRouter()

@router.get("/posts", response_model=List[Post])
async def get_posts(service = Depends(get_app_service)):
    return await service.get_posts()

@router.get("/posts/{id}", response_model=Post)
async def get_post(id: PyObjectId, service = Depends(get_app_service)):
    return await service.get_post(id)

@router.post("/posts", response_model=Post)
async def create_post(post: NewPost, service = Depends(get_app_service)):
    return await service.create_post(post)

@router.delete("/posts/{id}")
async def delete_post(id: PyObjectId, service = Depends(get_app_service)):
    return await service.delete_post(id)

@router.put("/posts/{id}", response_model=Post)
async def modify_post(id: PyObjectId, post: EditPost, service = Depends(get_app_service)):
    return await service.modify_post(id, post)