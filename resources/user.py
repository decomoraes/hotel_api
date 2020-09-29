from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp

atributos = reqparse.RequestParser()
atributos.add_argument('username', type = str, required = True, help = 'You need  to insert your username')
atributos.add_argument('password', type = str, required = True, help = 'You need  to insert your password')

class Users(Resource):


    def get(self):
        return {'Todos os Usuários': [user.json() for user in UserModel.query.all()]}


class User(Resource): 


    def get(self, username):
        user = UserModel.find_username(username)
        if user is not None:
            return user.json()
        return {'message': 'User not found'}, 404 # not found


    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'Oops, we have some problem here, try again.'}, 500 # internal error

            return {'message': 'This user was deleted.'}
        return {'message': 'This user was not found'}, 404


class UserRegister(Resource):


    def post(self):
        dados = atributos.parse_args()

        if UserModel.find_username(dados['username']):
            return {'message': 'The username: {}, already exists'.format(dados['username'])}

        user = UserModel(**dados)
        user.save_user()
        return {'message': 'The user created succesfully'}, 201 # Created


class UserLogin(Resource):


    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_username(dados['username'])

        if user and safe_str_cmp(user.password, dados['password']):
            token_de_acesso = create_access_token(identity = user.user_id)
            return {'access_token': token_de_acesso}, 200
        return {"message": "The username or password isn't correct"}, 401 # Unauthorized