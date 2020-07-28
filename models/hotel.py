from sql_alchemy import base

class HotelModel(base.Model):
    __tablename__ = 'list_hotels'
    hotel_id = base.Column(base.String, primary_key = True)
    name = base.Column(base.String(80))
    score = base.Column(base.Float(precision = 1))
    price = base.Column(base.Float(precision = 2))
    city = base.Column(base.String(40))


    def __init__(self, hotel_id, name, score, price, city):
        self.hotel_id = hotel_id
        self.name = name
        self.score = price
        self.price = price
        self.city = city


    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'score': self.score,
            'price': self.price,
            'city': self.city
        }


    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id = hotel_id).first()
        if hotel:
            return hotel
        else:
            return None


    # @staticmethod
    # def find_hotel(hotel_id):
    #     for for_hotel in list_hotels:
    #         if for_hotel['hotel_id'] == hotel_id:
    #             return for_hotel
    #     return None


    def save_hotel(self):
        base.session.add(self)
        base.session.commit()


    def update_hotel(self, name, score, price, city):
        self.name = name
        self.score = price
        self.price = price
        self.city = city


    def delete_hotel(self):
        base.session.delete(self)
        base.session.commit()