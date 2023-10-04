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

#registration with jwt
class UserRegistrationResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('second_name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        # Check if the username or email already exists in the database
        if User.query.filter_by(username=args['username']).first() is not None:
            return {'message': 'Username already exists'}, 400
        if User.query.filter_by(email=args['email']).first() is not None:
            return {'message': 'Email already exists'}, 400

        # Create a new User instance and add it to the database
        new_user = User(
            username=args['username'],
            email=args['email'],
            password=args['password'],
            phonenumber=args['phonenumber']
        )
        db.session.add(new_user)
        db.session.commit()

        # Generate an access token for the newly registered user
        access_token = create_access_token(identity=new_user.id)

        return {
            'message': 'User registered successfully',
            'access_token': access_token
        }, 201
#Home page backend
class Home(Resource):
    def get(self):
        response_message = {
            "message": "Welcome to the FuJi Store Inventory Management System API"
        }
        return make_response(response_message, 200)
    
class Suppliers(Resource):
    def get(self):
        suppliers=[]
        for supplier in Supplier.query.all():
            supplier_dict ={
                "id": supplier.id,
                "logo": supplier.logo,
                "name": supplier.name,
                "contact": supplier.contact
            }
            suppliers.append(supplier_dict)
        return make_response(jsonify(suppliers), 200)

    
        
    



api.add_resource(Home, '/')
api.add_resource(Suppliers, '/suppliers')
api.add_resource(UserRegistrationResource, '/register')

if __name__ == '__main__':
    app.run(port=5555)
