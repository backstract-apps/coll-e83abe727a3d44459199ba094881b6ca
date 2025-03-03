from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Employees(BaseModel):
    id: int
    name: str
    employee_id: int
    age: int
    username: str
    password: str
    emailid: str


class ReadEmployees(BaseModel):
    id: int
    name: str
    employee_id: int
    age: int
    username: str
    password: str
    emailid: str
    class Config:
        from_attributes = True


class Students(BaseModel):
    id: int
    user: str
    password: str


class ReadStudents(BaseModel):
    id: int
    user: str
    password: str
    class Config:
        from_attributes = True




class PostEmployees(BaseModel):
    id: str
    name: str
    employee_id: str
    age: str
    username: str
    password: str
    emailid: str

    class Config:
        from_attributes = True



class PutEmployeesId(BaseModel):
    id: str
    name: str
    employee_id: str
    age: str
    username: str
    password: str
    emailid: str

    class Config:
        from_attributes = True



class PostStudents(BaseModel):
    id: str
    user: str
    password: str

    class Config:
        from_attributes = True



class PutStudentsId(BaseModel):
    id: str
    user: str
    password: str

    class Config:
        from_attributes = True

