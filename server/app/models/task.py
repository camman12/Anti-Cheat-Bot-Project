from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    keywords = db.Column(db.Text, nullable=False)
    delay_sec = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id
