from flask import Flask, request, jsonify, make_response 
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity  
from flask_cors import CORS
from models import db, User, Product, Supplier,  Shipping 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'
jwt = JWTManager(app)

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'
jwt = JWTManager(app)

# #handle registration process
# class UserRegistrationResource(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', type=str, required=True)
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
#             first_name=args['first_name'],
#             second_name=args['second_name'],
#             email=args['email'],
#             password=args['password']
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
    
class Products(Resource):
   # @jwt_required
    def get(self):
        products = []
        for product in Product.query.all():
            product_dict ={
                "id": product.id,
                "image": product.image,
                "product_name": product.product_name,
                "description": product.description,
                "type": product.type,
                "minimum_stock": product.minimum_stock,
                "supplier": product.supplier_id,
                "quantity": product.quantity,
            }
            products.append(product_dict)
        return make_response(jsonify(products), 200)
         
class ProductById(Resource):
    #@jwt_required
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
                "minimum_stock": product.minimum_stock,
            }
            return make_response(jsonify(product_dict), 200)
        else:
            return make_response(jsonify({"error": "Product not found"}),404)
    #@jwt_required
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
        
    #@jwt_required
    def delete (self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
          return {'message': 'Product not found'}, 404
        else:
            db.session.delete(product)
            db.session.commit()
            return {'message': 'Product deleted successfully'}
        

        
    
class Suppliers(Resource):
    #@jwt_required
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
    def post(self):
            data = request.get_json()

            # Validate the incoming data, ensuring it contains the required fields
            if 'logo' not in data or 'name' not in data or 'contact' not in data:
                return {'message': 'Missing required fields for supplier'}, 400

            # Create a new Supplier instance
            new_supplier = Supplier(
                logo=data['logo'],
                name=data['name'],
                contact=data['contact']
            )
            supplier_dict ={
                "id": new_supplier.id,
                "logo":new_supplier.logo,
                "name": new_supplier.name,
                "contact": new_supplier.contact
            }
            # Add the new supplier to the database
            db.session.add(new_supplier)
            db.session.commit()

            # Respond with a success message
            return make_response(jsonify(supplier_dict), 200)  
    
class SupplierById(Resource):
    #@jwt_required
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
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('product_name', type=str, required=True)
        parser.add_argument('image', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('quantity', type=int, required=True)
        parser.add_argument('minimum_stock', type=int, required=True)
        parser.add_argument('type', type=str, required=True)
        args = parser.parse_args()

        # Check if the supplier exists
        supplier = Supplier.query.filter_by(id=id).first()
        if not supplier:
            return {'message': 'Supplier not found'}, 404

        # Create a new Product instance and associate it with the supplier
        new_product = Product(
            product_name=args['product_name'],
            description=args['description'],
            quantity=args['quantity'],
            minimum_stock=args['minimum_stock'],
            image=args['image'],
            type=args['type'],
            supplier_id=id  # Set the supplier_id to the ID from the URL
        )
        product_dict ={
                "id": new_product.id,
                "image": new_product.image,
                "product_name": new_product.product_name,
                "description": new_product.description,
                "type": new_product.type,
                "minimum_stock": new_product.minimum_stock,
                "supplier": new_product.supplier_id,
                "quantity": new_product.quantity,
            }

        # Add the new product to the database
        db.session.add(new_product)
        db.session.commit()    
        return  make_response(jsonify(product_dict), 200)
        
    #edit supplier details 
    #@jwt_required
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
        
    # def delete(self, id):
    #     supplier = Supplier.query.filter_by(id=id).first()

    #     if supplier:
    #         # Fetch the products associated with the supplier
    #         products = Product.query.filter_by(supplier_id=id).all()

    #         # Delete the products
    #         for product in products:
    #             db.session.delete(product)

    #         # Fetch the purchases associated with the supplier
    #         purchases = Purchase.query.filter_by(supplier_id=id).all()

    #         # Update the product_id to NULL for purchases
    #         for purchase in purchases:
    #             purchase.product_id = None  # Set product_id to NULL
    #             db.session.delete(purchase)

    #         # Delete the supplier
    #         db.session.delete(supplier)
    #         db.session.commit()

    #         return {'message': 'Supplier, its products, and purchases deleted successfully'}
    #     else:
    #         return make_response(jsonify({"error": "Supplier not found"}), 404)
# class Purchases(Resource):
#     #get all purchases
#     #@jwt_required
#     def get(self):
#         purchases=[]
#         for purchase in Purchase.query.all():
#             purchase_dict = {
#                 "id": purchase.id,
#                 "supplier_id": purchase.supplier_id,
#                 "product_id": purchase.product_id
#             }
#             purchases.append(purchase_dict)
#         return make_response(jsonify(purchases), 200)
            
            
# class PurchaseById(Resource):
#      #get one purchases
#     #@jwt_required
#     def get(self, id):
#         purchase = Purchase.query.filter_by(id=id).first()
#         if purchase:
#             purchase_dict ={
#                 "id": purchase.id,
#                 "supplier_id": purchase.supplier_id,
#                 "product_id": purchase.product_id
#             }
#             return make_response(jsonify(purchase_dict), 200)
#         else:
#             return make_response(jsonify({"error": "Purchase not found"}),404)

class Shippings(Resource):
    #@jwt_required
    #get all shippings 
    def get(self):
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
#api.add_resource(UserRegistrationResource, '/register')
#api.add_resource(UserLoginResource, '/login')
#api.add_resource(UserResource, '/user/<int:id>')
api.add_resource(Suppliers, '/suppliers', methods=['GET','POST'])

# api.add_resource(Purchases, '/purchases')
# api.add_resource(PurchaseById, '/purchases/<int:id>')
api.add_resource(SupplierById, '/suppliers/<int:id>',methods=['POST','GET'])
api.add_resource(Products, '/products', methods=['GET'])
api.add_resource(ProductById, '/products/<int:id>')
api.add_resource(Shippings, '/shippings')


if __name__ == '__main__':
    app.run(port=5555)
