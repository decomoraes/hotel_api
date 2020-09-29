from flask_restful import Resource, reqparse
from models.product import ProductModel


class Products(Resource):
    def get(self):
        return {'All products': [product.json() for product in ProductModel.query.all()]}


class Product(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type = str, required = True, help = 'You need  to insert a name')
    parser.add_argument('score', type = float, required = True, help = 'You need to insert a score')
    parser.add_argument('price', type = float)
    parser.add_argument('size')
    parser.add_argument('discount', type = float)
    parser.add_argument('brand')
    parser.add_argument('quantity', type = float)
    parser.add_argument('sold', type = float)


    def get(self, product_id):
        product = ProductModel.find_product(product_id)
        if product is not None:
            return product.json()
        return {'message': 'Product not found'}, 404 # not found


    def post(self, product_id):
        if ProductModel.find_product(product_id):
            return {'message': 'Product ID: {}, already exists.'.format(product_id.upper())}, 400 # bad request

        args = Product.parser.parse_args()
        new_product = ProductModel(product_id, **args)
        try:
            new_product.save_product()
        except:
            return {'message': 'Oops, we have some problem here, try again.'}, 500 # internal error
        return new_product.json()


    def put(self, product_id):
        args = Product.parser.parse_args()
        product_found = ProductModel.find_product(product_id)
        if product_found:
            product_found.update_product(**args)
            product_found.save_product()
            return product_found.json(), 200
        product = ProductModel(product_id, **args)
        try:
            product.save_product()
        except:
            return {'message': 'Oops, we have some problem here, try again.'}, 500 # internal error
        return product.json(), 201


    def delete(self, product_id):
        product = ProductModel.find_product(product_id)
        
        if product:
            try:
                product.delete_product()
            except:
                return {'message': 'Oops, we have some problem here, try again.'}, 500 # internal error

            return {'message': 'This product was deleted.'}
        return {'message': 'This product was not found'}, 404