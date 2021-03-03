import os
from flask import Flask
import flask_sqlalchemy
import flask_praetorian
import flask_cors

db = flask_sqlalchemy.SQLAlchemy()
guard = flask_praetorian.Praetorian()
cors = flask_cors.CORS()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    roles = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, server_default='true')

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, email):
        return cls.query.filter_by(email=email).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active


app = Flask(__name__, static_folder='../../client/build')
app.config['SECRET_KEY'] = 'secret'  # CHANGE THIS
app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}

guard.init_app(app, User)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(os.getcwd(), "database.sqlite")}'
db.init_app(app)

cors.init_app(app)

# Create example account
with app.app_context():
    db.create_all()

    if db.session.query(User).filter_by(email='user@example.com').count() < 1:
        db.session.add(User(
          email='user@example.com',
          password=guard.hash_password('strongpassword'),
          roles='admin'
        ))
    
    db.session.commit()


from app.views import index
from app.views.api import keyword, login, profile