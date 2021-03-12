from app import db


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, nullable=False)
    keyword = db.Column(db.Text, nullable=False)
    page = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id
