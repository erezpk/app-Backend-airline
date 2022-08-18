from flask import Flask
from config import secret_key,SQL,SQLALCHEMY_TRACK_MODIFICATIONS

class Config():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.secret_key = secret_key
