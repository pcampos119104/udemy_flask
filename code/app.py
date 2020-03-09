import os

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import JWTManager # jwt_required

from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from blacklist import BLACKLIST

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECK'] = ['access', 'refresh']
app.secret_key = 'pcampos'
api = Api(app)

db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()

jwt = JWTManager(app) # not creating /auth

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin':True}
    return {'is_admin':False}

@jwt.token_in_blacklist_loader
def check_if_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST

@jwt.expired_token_loader
def expire_token_callback():
    return jsonify({
        'description': 'The token has expired',
        'error': 'token_expired'
    }), 401

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(TokenRefresh, '/refresh')

if __name__ == '__main__':
    # app.run(port=5000, debug=True)
    app.run(host='0.0.0.0', debug=True, port=int(os.environ.get('PORT', 8080)))
