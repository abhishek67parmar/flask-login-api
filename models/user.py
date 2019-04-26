from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(256))

    def __init__(self,username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        return {'users':list(map(lambda x: {'username': x.username, 'password':x.password}, cls.query.all()))}


class RevokedTokenModel(db.Model):
    __tablename__='revoked_token'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(125))


    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls,jti):
        res = cls.query.filter_by(jti = jti).first()
        return res
