from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo_get_database import get_database
from bson import ObjectId

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, adjust as needed
    allow_headers=["*"],  # Allows all headers, adjust as needed
)

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@app.post("/")
def sanity_check() -> Union[dict, str]:
    """
    A simple sanity check endpoint to verify that the API is running.
    Returns a JSON response with a message.
    """
    return {"message": "API is running successfully!"}

@app.get("/userloops/")
def get_user_loops():
    """
    Get user loops from the database.
    """
    dbname = get_database()
    collection_name = dbname["user_1_loops"]
    user_loops = [serialize_doc(loop) for loop in collection_name.find()]
    return user_loops