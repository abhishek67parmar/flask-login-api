from flask_restful import Resource, reqparse
from models.employee import EmployeeModel
from flask_jwt_extended import jwt_required

parser =reqparse.RequestParser()
parser.add_argument('emp_name', type=str, required=True)
parser.add_argument('city', type=str, required=True)


class Employee(Resource):
    @jwt_required
    def get(self,id):
        emp = EmployeeModel.find_by_id(id)
        if not emp:
            return {'message':'Employee not found!! :( '}
        return emp.json()

    @jwt_required
    def post(self,id):
        edata = parser.parse_args()

        e = EmployeeModel.find_by_id(id)
        if e:
            return {'message': 'Employee already present!!'}

        emp = EmployeeModel(id, edata['emp_name'], edata['city'])

        emp.save_to_db()

        return {'message': 'Employee successfully added'}

    @jwt_required
    def put(self,id):
        emp = EmployeeModel.find_by_id(id)

        edata = parser.parse_args()

        if not emp:
            emp = EmployeeModel(id, edata['emp_name'], edata['city'])
            emp.save_to_db()
            return {'message': 'New Employee added successfully'}

        else:
            emp.emp_name = edata['emp_name']
            emp.city = edata['city']
            emp.save_to_db()
            return {'message': 'Employee updated successfully'}

    @jwt_required
    def delete(self,id):
        emp = EmployeeModel.find_by_id(id)
        if not emp:
            return {'message':'Employee not found!! :( '}

        emp.delete_from_db()
        return {'message':'Employee is deleted successfully!! :) '}


class EmployeeAll(Resource):
    def get(self):
        return EmployeeModel.allEmployee()
