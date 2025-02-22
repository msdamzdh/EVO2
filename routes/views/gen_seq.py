## Importing necessary libraries
import os
import requests
from csv import Error
from fastapi import APIRouter
from pydantic import BaseModel, Field


# Model definition for body of requests
# Limitation and constraints can be defined here
class Params(BaseModel):
    sequence: str = Field(default="ACTGACTGACTGACTG")
    num_tokens: int = Field(default=8)
    top_k: int = Field(default=1)
    enable_sampled_probs: bool = False

routher = APIRouter()

# this address send request to nvidia and return a dictionary response
@routher.post("/genSeq")
async def genSeq(parameters:Params):
    try:
        NVCF_RUN_KEY = os.getenv("NVCF_RUN_KEY")
        NVIDIA_URL = os.getenv("NVIDIA_URL")
        response = requests.post(
            url=NVIDIA_URL,
            headers={"Authorization": f"Bearer {NVCF_RUN_KEY}"},
            json=dict(parameters)
        )
        return dict(response.json())
    except Error:
         return Error()