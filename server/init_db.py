from contextlib import closing

import sqlite3
DATABASE = 'database.db'

def connect_db():
    return sqlite3.connect(DATABASE)


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('data.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

init_db()