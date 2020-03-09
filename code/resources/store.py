from flask_restful import Resource, reqparse
from models.store import StoreModel
from flask_jwt_extended import jwt_required, get_jwt_claims, jwt_optional, get_jwt_identity, fresh_jwt_required

class Store(Resource):
    @jwt_required
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    @fresh_jwt_required
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'Store exists'}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'Server problem'}, 500

        return store.json(), 201

    @fresh_jwt_required
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store deleted'}

class StoreList(Resource):
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        stores = [store.json() for store in StoreModel.find_all()]
        if user_id:
            return {'stores': stores}
        return {'stores': [store['name'] for store in stores],
                'message': 'More data if log in'}
