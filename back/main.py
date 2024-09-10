from flask import Flask, request
from models import Base, Birthday
from datetime import datetime
from sqlalchemy import create_engine, select, delete
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import Session

GOOD = { 'status': 200, 'msg': 'OK' }
BAD = { 'status': 500, 'msg': ':(' }

app = Flask(__name__)

engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool, echo=True)

Base.metadata.create_all(engine)

with Session(engine) as session:

    b = [Birthday() for i in range(0, 3)]
    b[0].name = 'Arthur'
    b[0].date = datetime.now()
    b[1].name = 'Ju'
    b[1].date = datetime.strptime('2000-05-24', '%Y-%m-%d')
    b[2].name = 'M'
    b[2].date = datetime.strptime('2000-11-13', '%Y-%m-%d')

    session.bulk_save_objects(b)
    session.commit()

import birthday
import motd

if __name__ == '__main__':
    app.run('127.0.0.1', 8000, debug=True)
