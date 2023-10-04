from app import app, db
from models import User, Product, Supplier, Purchase, Shipping 
from datetime import datetime
from sqlalchemy.orm import sessionmaker


with app.app_context():
    def delete_data():
# delete existing db data in rows
        print("Deleting data...")
        User.query.delete()
        Product.query.delete()
        Supplier.query.delete()
        Purchase.query.delete()
        Shipping.query.delete()

    def seed_data():
        print("🦸‍♀️ Seeding User...")
        user1 =User(first_name="joy", second_name="akinyi", username = "itsjoycoder", email="joyakinyi@mail.com", password="moringa20")
        user2 =User(first_name="felix", second_name="okeyo", username = "itsfelixayo", email="felixokeyo@mail.com", password="moringa21")
    
        user_list =[user1, user2]
        db.session.add_all(user_list)

        print("🦸‍♀️ Seeding products...")
        product1 = Product(image= "https://media.gettyimages.com/id/1279931147/photo/laptop-computer-blank-white-screen-on-table-in-cafe-background-laptop-with-blank-screen-on.jpg?s=612x612&w=gi&k=20&c=HT6AC8RHFzOFQIWAmeHVtVT7LQzWhqCL9Iv3EsDHo6E=",
                           product_name="Apple MacBook", description = "Apple MacBook Pro is a macOS laptop with a 13.30-inch display that has a resolution of 2560x1600 pixels. It is powered by a Core i5 processor and it comes with 12GB of RAM.",
                           type = "Laptop", supplier_id = 1, quantity = 5, minimum_stock = 3)
        product2 = Product(image="https://media.gettyimages.com/id/1299655397/photo/apps-installed-on-a-samsung-galaxy-s21-smart-phone.jpg?s=612x612&w=gi&k=20&c=T99tXxVDDkc9MCS3S4yF6tO0vmDnAFptmgDoBqrfr24=",
                           product_name = "Samsung Galaxy S21", description = "The Samsung Galaxy S21 specs are top-notch including a Snapdragon 888 chipset, 5G capability, 8GB RAM coupled with 128/256GB storage, and a 4000mAh battery. The phone sports a 6.2-inch Dynamic AMOLED display with an adaptive 120Hz refresh rate. In the camera department, a triple-sensor setup is presented",
                           type="Phone", supplier_id= 2,quantity=10, minimum_stock =5)
        product3 = Product(image="https://media.gettyimages.com/id/458405389/photo/lenovo-thinkpad-x201-notebook.jpg?s=612x612&w=gi&k=20&c=V9hldqn4eh0amsdIMWQxrbib8QoBe7FnBgwTPTHWVOk=",
                           product_name = "Lenovo ThinkPad X201 Notebook", description = "UltraNav combines a TrackPoint and a large multi-gesture TouchPad for precise cursor control. The computer is powered by a dual-core 2.66GHz Intel Core i5-560M CPU, which can be overclocked to 3.2GHz thanks to Intel Turbo Boost",
                           type="Laptop", supplier_id= 3, quantity=7, minimum_stock =2)
        product4 = Product(image="https://media.gettyimages.com/id/458405389/photo/lenovo-thinkpad-x201-notebook.jpg?s=612x612&w=gi&k=20&c=V9hldqn4eh0amsdIMWQxrbib8QoBe7FnBgwTPTHWVOk=",
                           product_name = "Lenovo ThinkPad X201 Notebook", description = "UltraNav combines a TrackPoint and a large multi-gesture TouchPad for precise cursor control. The computer is powered by a dual-core 2.66GHz Intel Core i5-560M CPU, which can be overclocked to 3.2GHz thanks to Intel Turbo Boost",
                           type="Laptop", supplier_id= 3, quantity=7, minimum_stock =2)
        product5 = Product(image="https://media.gettyimages.com/id/458405389/photo/lenovo-thinkpad-x201-notebook.jpg?s=612x612&w=gi&k=20&c=V9hldqn4eh0amsdIMWQxrbib8QoBe7FnBgwTPTHWVOk=",
                           product_name = "Lenovo ThinkPad X201 Notebook", description = "UltraNav combines a TrackPoint and a large multi-gesture TouchPad for precise cursor control. The computer is powered by a dual-core 2.66GHz Intel Core i5-560M CPU, which can be overclocked to 3.2GHz thanks to Intel Turbo Boost",
                           type="Laptop", supplier_id= 3, quantity=7, minimum_stock =2)
        product6 = Product(image="https://media.gettyimages.com/id/458405389/photo/lenovo-thinkpad-x201-notebook.jpg?s=612x612&w=gi&k=20&c=V9hldqn4eh0amsdIMWQxrbib8QoBe7FnBgwTPTHWVOk=",
                           product_name = "Lenovo ThinkPad X201 Notebook", description = "UltraNav combines a TrackPoint and a large multi-gesture TouchPad for precise cursor control. The computer is powered by a dual-core 2.66GHz Intel Core i5-560M CPU, which can be overclocked to 3.2GHz thanks to Intel Turbo Boost",
                           type="Laptop", supplier_id= 3, quantity=7, minimum_stock =2)
        product7 = Product(image="https://media.gettyimages.com/id/458405389/photo/lenovo-thinkpad-x201-notebook.jpg?s=612x612&w=gi&k=20&c=V9hldqn4eh0amsdIMWQxrbib8QoBe7FnBgwTPTHWVOk=",
                           product_name = "Lenovo ThinkPad X201 Notebook", description = "UltraNav combines a TrackPoint and a large multi-gesture TouchPad for precise cursor control. The computer is powered by a dual-core 2.66GHz Intel Core i5-560M CPU, which can be overclocked to 3.2GHz thanks to Intel Turbo Boost",
                           type="Laptop", supplier_id= 3, quantity=7, minimum_stock =2)
                           
        product_list = [product1, product2, product3,product4,product5,product6, product7]
        db.session.add_all(product_list)
        
        print("🦸‍♀️ Seeding suppliers...")

        supplier1= Supplier(logo="https://i.ytimg.com/vi/FzcfZyEhOoI/maxresdefault.jpg", name ="Apple", contact = "apple@apple.com")
        supplier2= Supplier(logo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoBVMEwdKDUtMN4CiYTcMKf4UHb8cASDG2mmVPIbwP-Rtfw4kAzH5Vr6DaqWtw_ufjQ3A&usqp=CAU",
                            name = "Samsung", contact ="samsung@gmail.com")
        supplier3= Supplier(logo = "https://media.istockphoto.com/id/1166473961/photo/lenovo-group-limited-headquarters-located-in-silicon-valley.jpg?s=612x612&w=0&k=20&c=WjecflgRHam4UfWNFMyk9ness8byvYyEkcgc1iivzqc=",
                            name = "Lenovo", contact = "lenovo@gmail.com")
        supplier4= Supplier(logo = "https://media.gettyimages.com/id/103012503/photo/illustration-picture-shows-the-headquarters-of-us-information-technology-giant-hewlett-packard.jpg?s=612x612&w=gi&k=20&c=n3xjWY22vlR1FOvcvRifhJFhDXCPz5ewJW-a8vqKbS0=",
                            name = "HP", contact ="hp@gmail.com")
        supplier5= Supplier(logo ="https://media.istockphoto.com/id/1310441327/photo/microsoft-france-headquarters-entrance-in-issy-les-moulineaux-near-paris.jpg?s=612x612&w=0&k=20&c=w4df4OwilAGtPb01aXv910ND85E9Vh0I8qZ4CuRbFqI=",
                            name = "Microsoft", contact ="microsoft@microsoft.com")
        supplier6= Supplier(logo ="https://thumbs.dreamstime.com/z/googleplex-google-headquarters-california-mountain-view-ca-usa-may-office-buildings-93111097.jpg",
                            name = "Google", contact = "contact@google.com")
        supplier7= Supplier(logo = "https://c8.alamy.com/comp/2DA48RJ/huawei-headquarters-building-2DA48RJ.jpg",
                            name ="Huawei", contact ="huawei@gmail.com")
        
        suppliers_list = [supplier1, supplier2, supplier3, supplier4, supplier5, supplier6, supplier7]
        db.session.add_all(suppliers_list)
        
        print("🦸‍♀️ Seeding shippings...")
        shipping1 = Shipping(product_id = 1, status = "In-Stock")
        shipping2 = Shipping(product_id = 2, status = "Sold")
        shipping3 = Shipping(product_id = 3, status = "Ordered")
        
        shipping_list= [shipping1, shipping2, shipping3]
        db.session.add_all(shipping_list)
        
        
        print("🦸‍♀️ Seeding purchases...")
        purchase1 = Purchase(supplier_id = 1, product_id=1)
        purchase2 = Purchase(supplier_id = 2, product_id=2)
        
        purchase_list= [purchase1, purchase2]
        db.session.add_all(purchase_list)
    
        
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.app = app # bind the app to current SQLAlchemy instance
        delete_data()
        db.session.commit()
        seed_data()
        db.session.commit()
        
        print("🦸‍♀️ Done seeding!")
