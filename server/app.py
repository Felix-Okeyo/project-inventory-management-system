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

#handle registration process
# class UserRegistrationResource(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('first_name', type=str, required=True)
#         parser.add_argument('second_name', type=str, required=True)
#         parser.add_argument('email', type=str, required=True)
#         parser.add_argument('password', type=str, required=True)
#         args = parser.parse_args()

#         # Check if the username or email already exists in the database
#         if User.query.filter_by(username=args['username']).first() is not None:
#             return {'message': 'Username already exists'}, 400
#         if User.query.filter_by(email=args['email']).first() is not None:
#             return {'message': 'Email already exists'}, 400

#         # Create a new User instance and add it to the database
#         new_user = User(
#             username=args['username'],
#             email=args['email'],
#             password=args['password'],
#             phonenumber=args['phonenumber']
#         )
#         db.session.add(new_user)
#         db.session.commit()

#         # Generate an access token for the newly registered user
#         access_token = create_access_token(identity=new_user.id)

#         return {
#             'message': 'User registered successfully',
#             'access_token': access_token
#         }, 201

# #handle the login requests
# class UserLoginResource(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', type=str, required=True)
#         parser.add_argument('password', type=str, required=True)
#         args = parser.parse_args()

#         user = User.query.filter_by(username=args['username']).first()

#         if user and user.password == args['password']:
#             access_token = create_access_token(identity=user.id)
#             return {'access_token': access_token}, 200
#         else:
#             return {'message': 'Invalid credentials'}, 401
        
# class UserResource(Resource):
#     @jwt_required()
#     def get(self, user_id):
#         user = User.query.get_or_404(user_id)
#         return user.as_dict()

#     @jwt_required()
#     def put(self, user_id):
#         user = User.query.get_or_404(user_id)
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', type=str)
#         parser.add_argument('email', type=str)
#         args = parser.parse_args()

#         for key, value in args.items():
#             if value is not None:
#                 setattr(user, key, value)

#         db.session.commit()
#         return {'message': 'User updated successfully'}

#     @jwt_required()
#     def delete(self, user_id):
#         user = User.query.get_or_404(user_id)
#         db.session.delete(user)
#         db.session.commit()
#         return {'message': 'User deleted successfully'}        


class Home(Resource):
    def get(self):
        response_message = {
            "message": "Welcome to the FuJi Store Inventory Management System API"
        }
        return make_response(response_message, 200)
    
class Suppliers(Resource):
    # @jwt_required
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

class SupplierById(Resource):
    # @jwt_required
    #get one supplier from db
    def get(self, id):
        supplier = Supplier.query.filter_by(id=id).first()
        if supplier:
            supplier_dict ={
                "id": supplier.id,
                "logo": supplier.logo,
                "name": supplier.name,
                "contact": supplier.contact
            }
            return make_response(jsonify(supplier_dict), 200)
        else:
            return make_response(jsonify({"error": "Supplier not found"}),404)
        
    #edit supplier details 
    # @jwt_required
    def patch(self, id):
        supplier = Supplier.query.filter_by(id=id).first()
        data = request.get_json()
        
        if supplier:
            for attr in data:
                setattr(supplier, attr, data[attr])
            
            db.session.add(supplier)
            db.session.commit()
            
            response_body = {
                "id": supplier.id,
                "logo": supplier.logo,
                "name": supplier.name,
                "contact": supplier.contact
            }
            return response_body, 201
        else:
            return make_response(jsonify({"error": "Supplier not found"}),404)
        
     # @jwt_required
    def delete (self, id):
        supplier = Supplier.query.filter_by(id=id).first()
        db.session.delete(supplier)
        db.session.commit()
        return {'message': 'Supplier deleted successfully'}
        

        
class Purchases(Resource):
    # @jwt_required
    def get(self):
        purchases=[]
        for purchase in Purchase.query.all():
            purchase_dict = {
                "id": purchase.id,
                "supplier_id": purchase.supplier_id,
                "product_id": purchase.product_id
            }
            purchases.append(purchase_dict)
        return make_response(jsonify(purchases), 200)
            




api.add_resource(Home, '/')
# api.add_resource(UserRegistrationResource, '/register')
# api.add_resource(UserLoginResource, '/login')
api.add_resource(Suppliers, '/suppliers')
api.add_resource(Purchases, '/purchases')
api.add_resource(SupplierById, '/suppliers/<int:id>')


if __name__ == '__main__':
    app.run(port=5555)
