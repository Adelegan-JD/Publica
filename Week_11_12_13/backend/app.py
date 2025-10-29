from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os
load_dotenv()
from database import db

app = FastAPI(title='Simple FastAPI App', description= 'This is my first API app', version='1.0.0')

data = [{'name': 'Adelegan Deborah', 'track': 'AI Engineering', 'age': 20}, 
{'name': 'Adelegan Abigail', 'track': 'Blockchain Developer', 'age': 21},
{'name': 'Adelegan Esther', 'track': '3D Specialist', 'age': 22}]


class item(BaseModel):
    name : str = Field(..., examples= 'Perpetual')
    track: str = Field(..., examples= 'Tech track')
    age: int = Field(..., examples= 12)



@app.get("/", description= 'This endpoint returns a welcome message and the data')
def root():
    return {'Message': 'Welcome to my FastAPI Application'}

@app.get("/get-data")
def get_data():
    return data

@app.post("/create-data")
def create_data(req: item):
    data.append(req.model_dump())
    return {'Message': 'Data received', 'Data': data}

@app.put("/update-data/{id}")
def update_data(id: int, req: item):
    data[id] = req.model_dump()
    print(data)
    return {'Message': 'Data Updated', 'Data': data}


if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port"))) # type: ignore
