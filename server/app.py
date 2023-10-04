from flask import Flask, request, jsonify, make_response 
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity  

from models import db, User, Product, Supplier, Purchase, Shipping 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'
jwt = JWTManager(app)

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'
jwt = JWTManager(app)

#Home page backend
class Home(Resource):
    def get(self):
        response_message = {
            "message": "Welcome to the Superheroes API"
        }
        return make_response(response_message, 200)
    
# class Suppliers(Resource):
#     def get(self):
    
        
    




# api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(port=5555)
