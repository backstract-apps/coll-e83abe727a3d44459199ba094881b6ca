from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_employees(db: Session):

    employees_all = db.query(models.Employees).all()
    employees_all = [new_data.to_dict() for new_data in employees_all] if employees_all else employees_all

    res = {
        'employees_all': employees_all,
    }
    return res

async def get_employees_id(db: Session, id: int):

    employees_one = db.query(models.Employees).filter(models.Employees.id == id).first() 
    employees_one = employees_one.to_dict() if employees_one else employees_one

    res = {
        'employees_one': employees_one,
    }
    return res

async def post_employees(db: Session, raw_data: schemas.PostEmployees):
    id:str = raw_data.id
    name:str = raw_data.name
    employee_id:str = raw_data.employee_id
    age:str = raw_data.age
    username:str = raw_data.username
    password:str = raw_data.password
    emailid:str = raw_data.emailid


    record_to_be_added = {'id': id, 'name': name, 'employee_id': employee_id, 'age': age, 'username': username, 'password': password, 'emailid': emailid}
    new_employees = models.Employees(**record_to_be_added)
    db.add(new_employees)
    db.commit()
    db.refresh(new_employees)
    employees_inserted_record = new_employees.to_dict()

    res = {
        'employees_inserted_record': employees_inserted_record,
    }
    return res

async def put_employees_id(db: Session, raw_data: schemas.PutEmployeesId):
    id:str = raw_data.id
    name:str = raw_data.name
    employee_id:str = raw_data.employee_id
    age:str = raw_data.age
    username:str = raw_data.username
    password:str = raw_data.password
    emailid:str = raw_data.emailid


    employees_edited_record = db.query(models.Employees).filter(models.Employees.id == id).first()
    for key, value in {'id': id, 'name': name, 'employee_id': employee_id, 'age': age, 'username': username, 'password': password, 'emailid': emailid}.items():
          setattr(employees_edited_record, key, value)
    db.commit()
    db.refresh(employees_edited_record)
    employees_edited_record = employees_edited_record.to_dict() 

    res = {
        'employees_edited_record': employees_edited_record,
    }
    return res

async def delete_employees_id(db: Session, id: int):

    employees_deleted = None
    record_to_delete = db.query(models.Employees).filter(models.Employees.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        employees_deleted = record_to_delete.to_dict() 

    res = {
        'employees_deleted': employees_deleted,
    }
    return res

async def get_students(db: Session):

    students_all = db.query(models.Students).all()
    students_all = [new_data.to_dict() for new_data in students_all] if students_all else students_all

    res = {
        'students_all': students_all,
    }
    return res

async def get_students_id(db: Session, id: int):

    students_one = db.query(models.Students).filter(models.Students.id == id).first() 
    students_one = students_one.to_dict() if students_one else students_one

    res = {
        'students_one': students_one,
    }
    return res

async def post_students(db: Session, raw_data: schemas.PostStudents):
    id:str = raw_data.id
    user:str = raw_data.user
    password:str = raw_data.password


    record_to_be_added = {'id': id, 'user': user, 'password': password}
    new_students = models.Students(**record_to_be_added)
    db.add(new_students)
    db.commit()
    db.refresh(new_students)
    students_inserted_record = new_students.to_dict()

    res = {
        'students_inserted_record': students_inserted_record,
    }
    return res

async def put_students_id(db: Session, raw_data: schemas.PutStudentsId):
    id:str = raw_data.id
    user:str = raw_data.user
    password:str = raw_data.password


    students_edited_record = db.query(models.Students).filter(models.Students.id == id).first()
    for key, value in {'id': id, 'user': user, 'password': password}.items():
          setattr(students_edited_record, key, value)
    db.commit()
    db.refresh(students_edited_record)
    students_edited_record = students_edited_record.to_dict() 

    res = {
        'students_edited_record': students_edited_record,
    }
    return res

async def delete_students_id(db: Session, id: int):

    students_deleted = None
    record_to_delete = db.query(models.Students).filter(models.Students.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        students_deleted = record_to_delete.to_dict() 

    res = {
        'students_deleted': students_deleted,
    }
    return res

