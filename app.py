from flask import Flask
from flask_restful import Api
from resources.hotel import Hotels, Hotel
from resources.product import Products, Product
from resources.user import Users, User, UserRegister, UserLogin
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def cria_banco():
    base.create_all()


api.add_resource(Products, '/products')
api.add_resource(Product, '/product/<string:product_id>')
api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotel/<string:hotel_id>')
api.add_resource(Users, '/users')
api.add_resource(User, '/auth/user/<string:username>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    from sql_alchemy import base
    base.init_app(app)
    app.run(debug = True)
    CORS(app)