from database import db

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
import bcrypt
from dotenv import load_dotenv
import uvicorn

from middleware import create_token, verify_token



load_dotenv()


app = FastAPI(title= "User Management App", version = "1.0.0")


class Simple(BaseModel):
    Name: str = Field(..., examples= ["Deborah Adelegan"])
    email: str = Field(..., examples=["deborah@gmail.com"])
    password: str = Field(..., examples= ["ade123"])
    usertype: str = Field(..., examples= ['student'])

class Login(BaseModel):
    email: str = Field(..., examples=["deborah@gmail.com"])
    password:str = Field(..., examples=[ "ade123"])

class courseRequest(BaseModel):
    title: str = Field(..., examples=["Machine Learning"])
    level: str = Field(..., examples=["400 level"])

@app.post("/signup")
def Signup(input:Simple):
    try:

        duplicate_query = text("""
            SELECT * FROM users WHERE email = :email""")

        existing = db.execute(duplicate_query, {"email": input.email}.fetchone())
        if existing:
            return HTTPException(status_code=400, detail= "Email already exists!")



        query = text("""
            INSERT INTO users(name, email, password)
            VALUES(:name, :email, :password)
                               """)
        

        salt= bcrypt.gen_salt()
        hashedPassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)

        try:
            db.execute(query, {"name": input.name, "email":input.email, "password":hashedPassword, 'usertype':input.usertype})
            db.commit()
            return ({'message': 'User created successfully'})
        except:
            db.rollback()
        finally:
            db.close()

    except Exception as e:
        raise HTTPException(status=500, detail= str(e))
    
@app.post('/login')
def login(input:Login):
    try:
        query = text("SELECT * FROM users WHERE email = :email")
        user = db.execute(query, {"email": input.email}.fetchone())

        if not user:
            raise HTTPException(status_code=401, detail= 'Invalid Password')
        
        encoded_token = create_token(details={'email': user.email, 'usertype': user.usertype}, expiry= 'token_time')

        return {'message': 'Login Successful', 
                'user':{
                    'id': user.id,
                    'name':user.name,
                    'email': user.email,
                    'usertype':user.usertype
                    },
                    'token': encoded_token
                    }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@app.post('/courses')
def add_courses(input: courseRequest, user_data = Depends(verify_token)):
    try:
        print(user_data)
        if user_data['usertype'] != 'admin':
            raise HTTPException(status_code=401, detail= 'You are not authorized to add a course')
        
        query = text("""
            INSERT INTO courses (title, level)
                        VALUES(:title, :level)
            """)

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail= str(e))
    finally:
        db.close()

# @app.post('/enroll')
# def enroll_token(input: )
# 

if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv("host"), port= int(os.getenv("port")))
