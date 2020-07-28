from flask_restful import Resource, reqparse
from models.user import UserModel


class Users(Resource):
    def get(self):
        return {'Todos os Usuários': [user.json() for user in UserModel.query.all()]}


class User(Resource):


    def get(self, user_id):
        user = UserModel.find_user(user_id)
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
        atributos = reqparse.RequestParser()
        atributos.add_argument('username', type = str, required = True, help = 'You need  to insert your username')
        atributos.add_argument('password', type = str, required = True, help = 'You need  to insert your password')
        dados = atributos.parse_args()

        if UserModel.find_username(dados['username']):
            return {'message': 'The username: {}, already exists'.format(dados['username'])}

        user = UserModel(**dados)
        user.save_user()
        return {'message': 'The user created succesfully'}, 201 # Created