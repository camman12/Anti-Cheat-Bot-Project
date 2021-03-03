from exts import db

class EntityBase(object):
    def to_json(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]
        return fields

class User(db.Model, EntityBase):
    #数据表明、字段
    __tablename__ = 'tp_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(255))
    mobile = db.Column(db.String(20))
