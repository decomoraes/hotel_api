from flask_restful import Resource, reqparse
from models.hotel import HotelModel


class Hotels(Resource):
    def get(self):
        return {'Todos os hotéis': [hotel.json() for hotel in HotelModel.query.all()]}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name', type = str, required = True, help = 'You need  to insert a name')
    argumentos.add_argument('score', type = float, required = True, help = 'You need to insert a score')
    argumentos.add_argument('price')
    argumentos.add_argument('city')


    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel is not None:
            return hotel.json()
        return {'message': 'Hotel not found'}, 404 # not found


    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': 'Hotel ID: {}, already exists.'.format(hotel_id.upper())}, 400 # bad request

        dados = Hotel.argumentos.parse_args()
        new_hotel = HotelModel(hotel_id, **dados)
        try:
            new_hotel.save_hotel()
        except:
            return {'message': 'Oops, we have some problem here, try again.'}, 500 # internal error
        return new_hotel.json()


    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_found = HotelModel.find_hotel(hotel_id)
        if hotel_found:
            hotel_found.update_hotel(**dados)
            hotel_found.save_hotel()
            return hotel_found.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'Oops, we have some problem here, try again.'}, 500 # internal error
        return hotel.json(), 201


    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'Oops, we have some problem here, try again.'}, 500 # internal error

            return {'message': 'This hotel was deleted.'}
        return {'message': 'This hotel was not found'}, 404