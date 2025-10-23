from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
import bcrypt
from dotenv import load_dotenv
import uvicorn


load_dotenv()

app = FastAPI(title='A simple App', version="1.0.0")


class Simple(BaseModel):
    name: str = Field(..., examples= "Debby Ade")
    email: str = Field(..., examples= "debby@gmail.com")
    password: str = Field(..., examples= "ade123")


@app.post("/signup")
def SignUp(input: Simple):
    try:
        query = text("""
        INSERT INTO users (name, email, password)
        VALUES (:name, :email, :password)
        """)

        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)
        print(hashedPassword)
        db.execute(query, {"name": input.name, "email": input.email, "password": hashedPassword})
        db.commit()

        return{"Message": "User details uploaded successfully", "data": {"name": input.name}, "email": input.email}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail = e)