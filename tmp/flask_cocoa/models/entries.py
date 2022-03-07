from flask_cocoa import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class Product(db.Model):
    __tablename__ = 'product'
    product_ID = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.Text, nullable=True)
    product_price = db.Column(db.Integer)
    picture_URL = db.Column(db.Text)
    product_description = db.Column(db.Text)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.Text)
    name = db.Column(db.Text)
    address = db.Column(db.Text, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def __init__(self, email=None, password=None, name=None, address=None):
        self.email = email
        self.password = password
        self.name = name
        self.address = address
        self.created_on = datetime.utcnow()

    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.username)

class Order(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.BigInteger, db.ForeignKey('product.product_ID'))
    transaction_id = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def __init__(self, product_id, transaction_id, quantity, user_id):
        self.product_id = product_id
        self.transaction_id = transaction_id
        self.quantity = quantity
        self.created_on = datetime.utcnow()
        self.user_id = user_id

