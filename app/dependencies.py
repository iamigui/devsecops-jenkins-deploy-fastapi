from functools import lru_cache
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from app.settings import Settings

@lru_cache()
def get_settings() -> Settings:
    return Settings()

@lru_cache()
def get_mongo_client(config: Settings = Depends(get_settings)):
    return AsyncIOMotorClient(config.mongo.url, serverSelectionTimeoutMS=5000)

@lru_cache()
def get_mongo_database(
    client=Depends(get_mongo_client), settings: Settings = Depends(get_settings)
):
    return client[settings.mongo.database]

@lru_cache
def get_app_collection(
        database=Depends(get_mongo_database), settings: Settings = Depends(get_settings)
):
    return database[settings.mongo.collection]

@lru_cache
def get_app_service(collection = Depends(get_app_collection)):
    from app.service.service import AppService
    return AppService(collection)