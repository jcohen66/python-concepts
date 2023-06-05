from fastapi import FastAPI, Path, Query, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from models import Employee, User
from mongoengine import connect
from mongoengine.queryset.visitor import Q
import json
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime,timedelta
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_password_hash(password):
    return pwd_context.hash(password)

app = FastAPI()
connect(db="hrms", host="localhost", port=27017)

def authenticate_user(username, password):
    try:
        user = json.loads(User.objects.get(Q(username=username)).to_json())
        return pwd_context.verify(password, user["password"])
    except User.DoesNotExist:
        return False

# openssl rand -hex 32
SECRET_KEY = "7a506e3af17947bcde83d05e9f2d49b1af225949625fe107d5f667537d3a9aad"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + expires_delta
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    
    if authenticate_user(username, password):
        access_token = create_access_token(
            data={"sub": username}, expires_delta=timedelta(minutes=30)
        )
        return {"access_token": access_token, "token_type":"bearer"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password.")

# @app.get("/")
# def home():
#     return {"message":"Hello World!"}

@app.get("/get_all_employees")
def get_all_employees():
    employees = Employee.objects().to_json()
    employees_list = json.loads(employees)
        
    return {"employees": employees_list}

@app.get("/get_employee/{emp_id}")
def get_employee(emp_id: int= Path(..., gt=0)):
    employee = Employee.objects.get(emp_id=emp_id)
    return {
        "emp_id": employee.emp_id,
        "name": employee.name,
        "age": employee.age,
        "teams": employee.teams,
    }
    
@app.get("/search_employees")
def search_employees(name: str, age: int=Query(None, gt=18)):
    employees = Employee.objects.filter(Q(name__icontains=name) | Q(age=age))
    employees_list = json.loads(employees.to_json())
        
    return {"employees": employees_list}

class NewEmployee(BaseModel):
    emp_id: int
    name: str
    age: int = Body(None, gt=18)
    teams: list
    
@app.post("/add_employee")
def add_employee(employee: NewEmployee):
    new_employee = Employee(emp_id=employee.emp_id,
                            name=employee.name,
                            age=employee.age,
                            teams=employee.teams)
    new_employee.save()
    
    return {"message": "Employee added successfully"}

# Pydantic model
class NewUser(BaseModel):
    username: str
    password: str

@app.post("/sign_up")
def sign_up(new_user: NewUser):
    user = User(username=new_user.username,
                password=get_password_hash(new_user.password))
    user.save()
    
    return {"message": "New user created successfully"}

@app.get("/")
def home(token: str = Depends(oauth2_scheme)):
    return {"message":"Hello World!"}