from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pymysql.constants import CLIENT
from dotenv import load_dotenv
import os


load_dotenv()

# Create a connection database (the dialect is mysql, the driver is pymysql)
# db_url = dialect+driver://dbuser;dbpassword;dbhost;dbport;dbname    This is the format of creating a url

db_url = f"mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}"
# engine = create_engine("mysql+pymysql://user:pw@host/db", pool_pre_ping=True)

engine = create_engine(db_url)

session = sessionmaker(bind=engine)

db = session()

# query = text("select * from user")
# user = db.execute(query).fetchall()

# print(user)

create_users = text("""

CREATE TABLE IF NOT EXISTS user ( 
    id INT PRIMARY KEY AUTO_INCREMENT ,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);
""")


create_courses = text("""

CREATE TABLE IF NOT EXISTS courses(
    course_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    title VARCHAR(100) NOT NULL,
    level VARCHAR(255) NOT NULL
    );                 
    """)


create_enrollment = text("""
CREATE TABLE IF NOT EXISTS enrollment(
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    userID INT,
    courseID INT,
    FOREIGN KEY (userID) REFERENCES user(id),
    FOREIGN KEY (courseID) REFERENCES courses(course_id)                                      
                          );
""")

db.execute(create_users)
db.execute(create_courses)
db.execute(create_enrollment)
db.commit()

