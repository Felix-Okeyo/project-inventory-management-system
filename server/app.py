from flask import Flask, request, jsonify, make_response 
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity  
from flask_cors import CORS 
from models import db, User, Product, Supplier, Purchase, Shipping 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'the-key-is-secret'

db.init_app(app)
CORS(app)
migrate = Migrate(app, db)

api = Api(app)
jwt = JWTManager(app)


#handle registration process
class UserRegistrationResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
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
        #Navigate to the login page
        # Create a new User instance and add it to the database
        new_user = User(
            username=args['username'],
            first_name=args['first_name'],
            second_name=args['second_name'],
            email=args['email'],
            password=args['password']
        )
        db.session.add(new_user)
        db.session.commit()

        # Generate an access token for the newly registered user
        access_token = create_access_token(identity=new_user.id)

        return {
            'message': 'User registered successfully',
            'access_token': access_token
        }, 201
        
#testing the JWT authentication separately
class TestJWT(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {'user_id': current_user}

#handle the login requests
class UserLoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        user = User.query.filter_by(username=args['username']).first()

        if user and user.password == args['password']:
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401
        
class UserResource(Resource):
    @jwt_required()
    def get(self, id):
        user = User.query.get_or_404(id)
        if user:
            user_dict = {
                "id": user.id,
                "first_name": user.first_name,
                "second_name": user.second_name,
                "username": user.username,
                "email": user.email,
                "password": user.password   
            }
            return make_response(jsonify(user_dict), 200)
        else:
            return make_response(jsonify({"error": "User not found"}),404)
   
    def put(self, id):
        user = User.query.get_or_404(id)
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        args = parser.parse_args()

        for key, value in args.items():
            if value is not None:
                setattr(user, key, value)

        db.session.commit()
        return {'message': 'User updated successfully'}

   
    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}        

class Home(Resource):
    def get(self):
        response_message = {
            "message": "Welcome to the JFx Store Inventory Management System API"
        }
        return make_response(response_message, 200)
    
class GetProducts(Resource):
    @jwt_required()
    def get(self):
        
        # print(get_jwt_identity(), '-'*30)
        
        products = []
        for product in Product.query.all():
            product_dict ={
                "id": product.id,
                "image": product.image,
                "product_name": product.product_name,
                "description": product.description,
                "type": product.type,
                "supplier": product.supplier_id,
                "quantity": product.quantity,
            }
            products.append(product_dict)
        return make_response(jsonify(products), 200)
    
    @jwt_required()
    def post(self):
        inputdata = request.get_json()
        
        new_product = Product(
            image = inputdata['image'],
            product_name = inputdata['product_name'],
            description = inputdata['description'],
            type = inputdata['type'],
            supplier_id = inputdata['supplier_id'],
            quantity = inputdata['quantity'],
            minimum_stock = inputdata['minimum_stock']                                     
        )
        
        db.session.add(new_product)
        db.session.commit()
        
        return make_response(jsonify(new_product), 200)   

class ProductById(Resource):
    @jwt_required()
    #get one product by id from db
    def get(self, id):
        product = Product.query.filter_by(id=id).first()
        if product:
            product_dict ={
                "id": product.id,
                "image": product.image,
                "description": product.description,
                "type": product.type,
                "supplier": product.supplier_id,
                "quantity": product.quantity,
            }
            return make_response(jsonify(product_dict), 200)
        else:
            return make_response(jsonify({"error": "Product not found"}),404)
    @jwt_required()
    def patch(self, id):
        product = Product.query.filter_by(id=id).first()
        data = request.get_json()
        
        if product:
            for attr in data:
                setattr(product, attr, data[attr])
            
            db.session.add(product)
            db.session.commit()
            
            response_body = {
                "id": product.id,
                "image": product.image,
                "description": product.description,
                "type": product.type,
                "supplier": product.supplier_id,
                "quantity": product.quantity,
            }
            return response_body, 201
        else:
            return make_response(jsonify({"error": "Product not found"}),404)
        
    @jwt_required()
    def delete (self, id):
        product = Product.query.filter_by(id=id).first()
        db.session.delete(product)
        db.session.commit()
        return {'message': 'Product deleted successfully'}
          
class GetSuppliers(Resource):
    @jwt_required()
    def get(self):
        
        print(get_jwt_identity(), '-'*30)
        
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
    @jwt_required()
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
    @jwt_required()
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
        
    @jwt_required()
    def delete (self, id):
        supplier = Supplier.query.filter_by(id=id).first()
        db.session.delete(supplier)
        db.session.commit()
        return {'message': 'Supplier deleted successfully'}
              
class GetPurchases(Resource):
    #get all purchases
    @jwt_required()
    def get(self):
        
        print(get_jwt_identity(), '-'*30)
        
        
        purchases=[]
        for purchase in Purchase.query.all():
            purchase_dict = {
                "id": purchase.id,
                "supplier_id": purchase.supplier_id,
                "product_id": purchase.product_id
            }
            purchases.append(purchase_dict)
        return make_response(jsonify(purchases), 200)
                     
class PurchaseById(Resource):
     #get one purchases
    @jwt_required()
    def get(self, id):
        purchase = Purchase.query.filter_by(id=id).first()
        if purchase:
            purchase_dict ={
                "id": purchase.id,
                "supplier_id": purchase.supplier_id,
                "product_id": purchase.product_id
            }
            return make_response(jsonify(purchase_dict), 200)
        else:
            return make_response(jsonify({"error": "Purchase not found"}),404)

class GetShippings(Resource):
    @jwt_required()
    # get all shippings 
    def get(self):
        
        # print(get_jwt_identity(), '-'*30)
          
        shippings = []
        for shipping in Shipping.query.all():
            shipping_dict = {
                "id": shipping.id,
                "product_id": shipping.product_id,
                "status": shipping.status,
                "created_at": shipping.created_at,
                "updated_at": shipping.updated_at
            }
            shippings.append(shipping_dict)
        return make_response(jsonify(shippings), 200)


api.add_resource(Home, '/')
api.add_resource(UserRegistrationResource, '/register')
api.add_resource(UserLoginResource, '/login')
api.add_resource(TestJWT, '/testjwt')
api.add_resource(UserResource, '/users/<int:id>')
api.add_resource(GetSuppliers, '/suppliers')
api.add_resource(GetPurchases, '/purchases')
api.add_resource(PurchaseById, '/purchases/<int:id>')
api.add_resource(SupplierById, '/suppliers/<int:id>')
api.add_resource(GetProducts, '/products')
api.add_resource(ProductById, '/products/<int:id>')
api.add_resource(GetShippings, '/shippings')


if __name__ == '__main__':
    app.run(port=5555)
