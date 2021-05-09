from flask import request
from flask_praetorian import auth_required, current_user
from app import app, db, Task


@app.route('/api/crawler', methods=['POST'])
@auth_required
def crawler():
    user = current_user()
    keywords = request.form['keywords']
    delay_sec = request.form['delay_sec']

    try:
        delay_sec = int(delay_sec)
    except Exception:
        delay_sec = 1

    task = Task(
        user=user,
        keywords=keywords,
        delay_sec=delay_sec,
        status=0,
    )

    db.session.add(task)
    db.session.commit()

    return {'message': 'task added'}
