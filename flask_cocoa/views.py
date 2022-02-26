from flask import request, redirect, url_for, render_template, flash, session
from flask_cocoa import app
from flask_cocoa import db
from flask_cocoa.models.entries import Product


@app.route('/')
def show_entries():
	data = Product.query.all()
	return render_template('entries/index.html',data=data)

@app.route('/{product_ID}')
def show_item():
	# data = Product.query(Product).filter(Product.product_ID.where(product_ID={{product_ID}}))
	data = Product.query.all()
	return render_template('entries/product.html')