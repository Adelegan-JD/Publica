from database import db

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
import bcrypt
from dotenv import load_dotenv
import uvicorn
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pymysql.constants import CLIENT
from dotenv import load_dotenv
import os


load_dotenv()


app = FastAPI(title= "Simple App", version = "1.0.0")


class Simple(BaseModel):
    Name: str = Field(..., examples= "Deborah Adelegan")
    email: str = Field(..., examples="deborah@gmail.com")
    password: str = Field(..., examples= "ade123")


@app.post("/signup")
def Signup(input:Simple):
    try:

        duplicate_query = text("""
            SELECT * FROM users WHERE email = :email""")

        existing = db.execute(duplicate_query, {"email": input.email})
        if existing:
            result("Email already exists!")



        query = text("""
            INSERT INTO users(name, email, password)
            VALUES(:name, :email, :password)
                               """)
        

        salt= bcrypt.gen_salt()
        hashedPassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)


        db.execute(query, {"name": input.name, "email":input.email, "password":hashedPassword})

    except Exception as e:
        raise HTTPException(status=500, detail= str(e))
    

    if __name__ == __main__:
        uvicorn.run(app, host=os.getenv("host"), port= int(os.getenv("port")))
