import sys
from flask import Flask
import flask_sqlalchemy
import flask_praetorian
import flask_cors
from flask_apscheduler import APScheduler


app = Flask(__name__, static_folder='../../client/build')

# Import config
try:
    app.config.from_object('config')
except ImportError as e:
    print(e)
    print('Error loading configuration!')
    print('Does the file exist?')
    sys.exit(1)

db = flask_sqlalchemy.SQLAlchemy()
guard = flask_praetorian.Praetorian()
cors = flask_cors.CORS()

from app.models import User, Data, Task  # noqa

guard.init_app(app, User)
db.init_app(app)

cors.init_app(app)

# 初始化Flask-APScheduler，定时任务
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

# Create example user
with app.app_context():
    db.create_all()

    if db.session.query(User).filter_by(email='user@example.com').count() < 1:
        db.session.add(User(
          email='user@example.com',
          password=guard.hash_password('strongpassword'),
          roles='admin'
        ))

    db.session.commit()


from app.views import index  # noqa
from app.views.api import keyword, login, profile  # noqa
