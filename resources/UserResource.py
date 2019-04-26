from flask_restful import Resource,reqparse
from models.user import UserModel,RevokedTokenModel
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

parser = reqparse.RequestParser()
parser.add_argument('username',
    type=str,
    required=True,
    help='field can not be blank'
)
parser.add_argument('password',
    type=str,
    required=True,
    help='field can not be blank'
)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        pwd= sha256.hash(data['password'])

        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}

        user = UserModel(username= data['username'], password= pwd )
        user.save_to_db()
        access_token= create_access_token(identity=data['username'])
        refresh_token= create_refresh_token(identity=data['username'])
        return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()

        user = UserModel.find_by_username(data['username'])

        if not user:
            return {'message': 'User {} does not exist'.format(data['username'])}

        if sha256.verify(data['password'],user.password):
            access_token= create_access_token(identity=data['username'])
            refresh_token= create_refresh_token(identity=data['username'])
            return {
                    'message': 'User {} logged in'.format(data['username']),
                    'access_token': access_token,
                    'refresh_token': refresh_token
                    }
        else:
            return {'message': 'Invalid credentials'}


class LogoutAccessToken(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']

        revoked_token = RevokedTokenModel(jti = jti)
        revoked_token.add()
        return {'message': 'Access Token is revoked'}

class LogoutRefreshToken(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']

        revoked_token = RevokedTokenModel(jti = jti)
        revoked_token.add()
        return {'message': 'Refresh Token is revoked'}


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        user= get_jwt_identity()
        access_token= create_access_token(identity=user)
        return {'access_token': access_token}

class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()




class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }
