import os
from flask import send_from_directory, request, g
from app import app

import uuid
import sqlite3

import jwt
from jwt import PyJWTError
from datetime import datetime, timedelta

from requests_html import HTMLSession
from parsel import Selector
import pandas as pd
import time
import json

screct_key = "test"

DATABASE = 'database.db'


def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()
    print(request.headers.get('Token'))
    if request.url.find('login') >= 0 or request.url.find('registe') >= 0:
        return None
    if request.headers.get('Token') != None and len(request.headers.get('Token')) > 0:
        token = request.headers['Token']
        print('x-token')
        try:
            data = jwt.decode(token, key=screct_key, algorithms='HS256')
            g.user = data
            return None
        except PyJWTError:
            return 'login outdate, please relogin'
    else:
        return 'please login'
    return None

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    # Send static files if they exist, else send index.html
    if path != '' and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/registe',methods = ['POST'])
def registe():
    if request.method == 'POST':
        userid = str(uuid.uuid4())
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user (id,username,password) VALUES (?,?,?)",(userid,username,password) )

            con.commit()
            msg = "Record successfully added"
        return msg


# 生成token

@app.route('/login',methods = ['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = query_db('select * from user where USERNAME = ?',
                        [username], one=True)
        if user is None:
            return "no user"
        else:
            if password == user['PASSWORD']:
                
                payload = {  # jwt设置过期时间的本质 就是在payload中 设置exp字段, 值要求为格林尼治时间
                    "user_id": user['ID'],
                    'username': user['USERNAME'],
                    'exp': datetime.utcnow() + timedelta(seconds=30 * 60 * 60)
                }
                token = jwt.encode(payload, key=screct_key, algorithm='HS256')
                return token
            else:
                return 'false'
        # with sqlite3.connect("database.db") as con:
        #     cur = con.cursor()
        #     cur.execute("SELECT * FROM user where username = ?",(username) )

        #     con.commit()
        #     msg = "Record successfully added"
        # return msg


# for user in query_db('select * from users'):
#     print user['username'], 'has the id', user['user_id']

@app.route('/info',methods = ['GET'])
def info():
    return g.user

@app.route('/crawler',methods = ['POST'])
def crawler():
    task_id = str(uuid.uuid4())
    userid = g.user['user_id']
    keywords_str = request.form['keywords']
    delay_sec = request.form['delay_sec']
    try:
        delay_sec = int(delay_sec)
    except:
        delay_sec = 1
    keywords = keywords_str.split(',')
    
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO task (task_id,userid,keywords,delay_sec, status) VALUES (?,?,?,?,?)",(task_id,userid,keywords_str,delay_sec, 0) )

        con.commit()
        msg = "task added"
    return msg
    # c = Crawler(keywords, delay_sec)
    # ret = json.dumps(c.main())
    # return ret

@app.route('/get_res',methods = ['POST'])
def get_res():
    keywords_str = request.form['keywords']
    keywords = keywords_str.split(',')
    keywords_query = "','".join(keywords)

    datas = query_db('select * from datas where keyword in(\'' + keywords_query + '\')')
    
    return json.dumps(datas)