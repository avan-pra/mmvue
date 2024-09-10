from flask import Flask, request
from models import Base, Birthday
from datetime import datetime
from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import Session
from __main__ import app, engine

GOOD = { 'status': 200, 'msg': 'OK' }
BAD = { 'status': 500, 'msg': ':(' }

motd = 'This is the motd, change it !'

@app.route('/motd', methods=['GET'])
def get_motd():
    global motd
    resp = GOOD
    resp['data'] = motd
    return resp, 200

@app.route('/motd', methods=['POST'])
def post_motd():
    global motd
    data = request.get_json()
    motd = data['motd']
    return GOOD, 200
