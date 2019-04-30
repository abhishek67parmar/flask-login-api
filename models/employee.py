from db import db

class EmployeeModel(db.Model):
    __tablename__ = "employee"

    id =db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.String(7),unique=True)
    emp_name =db.Column(db.String(50))
    city = db.Column(db.String(30))


    def __init__(self,emp_id,emp_name,city):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.city = city

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def json(self):
        return {'emp_id':self.emp_id, 'emp_name':self.emp_name, 'city':self.city}


    @classmethod
    def find_by_id(cls,emp_id):
        return cls.query.filter_by(emp_id = emp_id).first()

    @classmethod
    def allEmployee(cls):
        return {'Employees':list(map(lambda x:{'emp_id':x.emp_id, 'emp_name':x.emp_name, 'city':x.city}, cls.query.all()))}
