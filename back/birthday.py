from flask import Flask, request
from models import Base, Birthday
from datetime import datetime
from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import Session
from __main__ import app, engine

GOOD = { 'status': 200, 'msg': 'OK' }
BAD = { 'status': 500, 'msg': ':(' }

@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    stmt = select(Birthday)
    birthdays = []
    for birthday in Session(engine).scalars(stmt).all():
        birthdays.append(birthday.to_dict())
    resp = GOOD
    resp['data'] = birthdays
    return resp, 200

@app.route('/birthdays', methods=['POST'])
def post_birthdays():
    data = request.get_json()
    with Session(engine) as session:
        b = Birthday()
        b.name = data['name']
        b.date = datetime.strptime(data['date'], '%Y-%m-%d')
        session.add(b)
        session.commit()
    return GOOD, 200

@app.route('/birthdays/<int:birthday>', methods=['DELETE'])
def delete_birthdays(birthday: int):
    stmt = delete(Birthday).where(Birthday.id == birthday)
    Session(engine).execute(stmt)
    return GOOD, 200
