from flask_cocoa import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'product'
    product_ID = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.Text, nullable=True)
    product_price = db.Column(db.Integer)
    picture_URL = db.Column(db.Text)
    product_description = db.Column(db.Text)
