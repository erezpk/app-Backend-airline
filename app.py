from __init__ import Config
from db import db   
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager


# <-------------<----Resources---->-------------->

from Resource.Flights import Flights,Flight
from Resource.Users import User,Users
from Resource.Customers import Customer,Customers,Customer_by
from Resource.Tickets import Ticket,Tickets
from Resource.Airline import Airlines,Airline,Airline_by_user_id 
from Resource.Countries import Country,Countries
from Resource.Adminstrator import Admin,Admins
from Resource.Users_Roles import Users_Roles
from Resource.security.user_login import  User_Login


app = Config.app
api = Api(app)
JWTManager(app)
cors = CORS(app, resources={r"/*" : {"origins": "*"}})


# -----------Routs--------------

@app.before_first_request
def create_tables():
    db.init_app(app)
    db.create_all()
    

# ------------------API--------------
api.add_resource(Countries,'/all_countries')
api.add_resource(Country,'/country','/country/<string:name>')

api.add_resource(Flights,'/all_fligths')
api.add_resource(Flight,'/fligth','/fligth/<int:id>')


api.add_resource(User_Login,'/login')

api.add_resource(Airlines,'/all_airlines')  
api.add_resource(Airline,'/airline','/airline/<string:name>')
api.add_resource(Airline_by_user_id,'/airline_by_user_id/<string:user_id>')

api.add_resource(Users,'/all_users')
api.add_resource(User,'/user','/user/<string:username>','/user/<string:username>/<string:password>','/user/<int:id>')

api.add_resource(Customer,'/customer','/customer/<int:id>')
api.add_resource(Customers,'/all_customers')
api.add_resource(Customer_by,'/customer_by_user_id/<int:id>')

api.add_resource(Ticket,'/ticket/<int:id>','/ticket')
api.add_resource(Tickets,'/all_tickets')

api.add_resource(Admin,'/admin/<int:id>','/admin')
api.add_resource(Admins,'/all_admins')


api.add_resource(Users_Roles,'/all_users_roles')

if __name__ == '__main__':  
    app.run(port=5000)
