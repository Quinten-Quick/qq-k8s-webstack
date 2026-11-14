import os
import socket
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo-svc:27017")
client = MongoClient(MONGO_URI)
db = client["webstack"]
users_collection = db["users"]

class UserResponse(BaseModel):
    name: str

@app.get("/api/user")
def get_user():
    user = users_collection.find_one()

    if user is None:
        return {"name": "Onbekend"}
    
    return {"name": user["name"]}


@app.get("/api/container")
def get_container():
    container_id = socket.gethostname()
    return {"container_id": container_id}

@app.get("/health")
def health_check():
    return {"status": "ok"}
