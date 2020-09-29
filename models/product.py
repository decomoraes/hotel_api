from sql_alchemy import base

class ProductModel(base.Model):
    __tablename__ = 'products_list'
    product_id = base.Column(base.String, primary_key = True)
    name = base.Column(base.String(80))
    score = base.Column(base.Float(precision = 1))
    price = base.Column(base.Float(precision = 2))
    size = base.Column(base.String(40))
    discount = base.Column(base.Float(precision = 2))
    brand = base.Column(base.String(40))
    quantity = base.Column(base.Float(precision = 2))
    sold = base.Column(base.Float(precision = 2))


    def __init__(self, product_id, name, score, price, size, discount, brand, quantity, sold):
        self.product_id = product_id
        self.name = name
        self.score = score
        self.price = price
        self.size = size
        self.discount = discount
        self.brand = brand
        self.quantity = quantity
        self.sold = sold


    def json(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'score': self.score,
            'price': self.price,
            'size': self.size,
            'discount': self.discount,
            'brand': self.brand,
            'quantity': self.quantity,
            'sold': self.sold
        }


    @classmethod
    def find_product(cls, product_id):
        product = cls.query.filter_by(product_id = product_id).first()
        if product:
            return product
        else:
            return None
        # return product or None


    # @staticmethod
    # def find_product(product_id):
    #     for for_product in list_products:
    #         if for_product['product_id'] == product_id:
    #             return for_product
    #     return None


    def save_product(self):
        base.session.add(self)
        base.session.commit()


    def update_product(self, name, score, price, size, discount, brand, quantity, sold):
        self.name = name
        self.score = score
        self.price = price
        self.size = size
        self.discount = discount
        self.brand = brand
        self.quantity = quantity
        self.sold = sold


    def delete_product(self):
        base.session.delete(self)
        base.session.commit()