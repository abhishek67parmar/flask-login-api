import os
from flask import Flask,jsonify
from flask_restful import Api
from resources.UserResource import UserLogin, UserRegistration, LogoutAccessToken, LogoutRefreshToken, TokenRefresh, AllUsers, SecretResource
from resources.employeeResource import Employee,EmployeeAll
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from models.user import RevokedTokenModel


app = Flask(__name__)
api= Api(app)
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL','sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False
app.config['SECRET_KEY']= 'SOMETHING-COMPLEX'
app.config['JWT_SECRET_KEY'] = 'SOM3TH!NG-V3RY-COMPL3X'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECK']= ['access','refresh']


# @app.before_first_request
# def create_table():
#     db.create_all()

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti =decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin,'/login')
api.add_resource(LogoutAccessToken,'/ATlogout')
api.add_resource(LogoutRefreshToken,'/RTlogout')
api.add_resource(TokenRefresh,'/refreshToken')
api.add_resource(AllUsers,'/allusers')
api.add_resource(Employee,'/employee/<string:id>')
api.add_resource(EmployeeAll,'/allEmployee')


if __name__ =="__main__":
    from db import db
    db.init_app(app)
    app.run()
