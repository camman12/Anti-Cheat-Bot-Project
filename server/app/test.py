from crawler.google import Crawler

import sqlite3
DATABASE = 'database.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def query_db(query, args=(), one=False):
    db = connect_db()
    cur = db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

def shishi():
  
    datas = query_db('select * from task where status = 0')
    query_db('update task set status = 1')

    for data in datas:
        # print(data)
        print(data['task_id'])
        print(data['keywords'])
        print(data['delay_sec'])
        task_id = data['task_id']
        keywords = data['keywords'].split(',')
        delay_sec = data['delay_sec']
        c = Crawler(task_id, keywords, delay_sec)
        c.main()