from flask_cocoa import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'TC_product'
    product_ID = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=True)
    product_price = db.Column(db.Integer)
    product_description = db.Column(db.VARCHAR(255))

    # def __init__(self, title=None, text=None):
    #     self.title = title
    #     self.text = text
    #     self.created_at = datetime.utcnow()

    # def __repr__(self):
    #     return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)