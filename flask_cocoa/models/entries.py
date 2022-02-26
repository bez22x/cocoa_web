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
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    # def __init__(self, title=None, text=None):
    #     self.title = title
    #     self.text = text
    #     self.created_at = datetime.utcnow()

    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.username)
