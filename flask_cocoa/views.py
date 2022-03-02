from typing import Dict, Any, Union

from flask import request, redirect, url_for, render_template, flash, session
from flask_cocoa import app
from flask_cocoa import db, mongo
from flask_cocoa.forms import SignupForm, LoginForm
from flask_cocoa.models.entries import Product, User, Order
from flask_login import current_user, login_user, login_required, logout_user
from flask_cocoa import login_manager
import uuid


@app.route('/')
def home_page():
    data = Product.query.all()
    return render_template('entries/index.html', data=data)


@app.route('/<int:product_ID>')
def show_item(product_ID):
    item = Product.query.filter_by(product_ID=str(product_ID)).first()
    like_item = mongo.db.if_you_like.find_one({'product_id': product_ID})
    like_items = [Product.query.filter_by(product_ID=product_id).first() for product_id in like_item['collaborative_filtering_list']]
    return render_template('entries/product.html', item=item, data=like_items)


@app.route('/product_list')
def show_entries():
    items = Product.query.all()
    return render_template('entries/product_list.html', items=items)


@app.route('/hot_list')
def show_hot():
    hot_items = mongo.db.hot_commodity.find().sort('amount', -1)
    hot_items = hot_items[:5]
    hot_items = [Product.query.filter_by(product_ID=item['product_id']).first() for item in hot_items]
    return render_template('entries/hot_list.html', items=hot_items)


@app.route('/shopping_cart')
def show_shopping_cart():
    return render_template('entries/shopping_cart.html')


@app.route('/add_cart', methods=["POST"])
def add_cart():
    item_quantity = int(request.form['quantity'])
    item_id = request.form['id']
    if item_quantity and item_id and request.method == 'POST':
        item = Product.query.filter_by(product_ID=item_id).first()
        item_dict = {
            item_id: {'name': item.product_name, 'id': item.product_ID, 'picture': item.picture_URL,
                      'quantity': item_quantity, 'price': item.product_price,
                      'total_price': item_quantity * item.product_price}}

        all_total_price = 0
        all_total_quantity = 0

        session.modified = True
        if 'cart_item' in session:
            if item_id in session['cart_item']:
                for key, value in session['cart_item'].items():
                    if item_id == key:
                        session.modified = True
                        old_quantity = session['cart_item'][key]['quantity']
                        total_quantity = old_quantity + item_quantity
                        session['cart_item'][key]['quantity'] = total_quantity
                        session['cart_item'][key]['total_price'] = total_quantity * item.product_price
            else:
                session['cart_item'].update(item_dict)

            for key, value in session['cart_item'].items():
                individual_quantity = int(session['cart_item'][key]['quantity'])
                individual_price = int(session['cart_item'][key]['total_price'])
                all_total_quantity = all_total_quantity + individual_quantity
                all_total_price = all_total_price + individual_price
        else:
            session['cart_item'] = item_dict
            all_total_quantity = all_total_quantity + item_quantity
            all_total_price = all_total_price + item_quantity * item.product_price

        session['all_total_quantity'] = all_total_quantity
        session['all_total_price'] = all_total_price

        return redirect(request.referrer)
    else:
        return '購物車添加錯誤'


@app.route('/empty_cart')
def empty_cart():
    del session['cart_item']
    del session['all_total_quantity']
    del session['all_total_price']
    return redirect(request.referrer)


@app.route('/del_product/<item_id>')
def del_product(item_id):
    all_total_price = 0
    all_total_quantity = 0
    session.modified = True

    for product_id, item in session['cart_item'].items():
        if product_id == item_id:
            session['cart_item'].pop(product_id, None)
            if 'cart_item' in session:
                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = int(session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
            break

    if all_total_quantity == 0:
        return redirect(url_for('empty_cart'))
    session['all_total_quantity'] = all_total_quantity
    session['all_total_price'] = all_total_price
    return redirect(request.referrer)

@app.route('/check_out')
@login_required
def check_out():
    transaction_id = uuid.uuid4()
    for key, value in session['cart_item'].items():
        order = Order(
            product_id=int(key),
            transaction_id=transaction_id,
            quantity=int(session['cart_item'][key]['quantity']),
            user_id=current_user.get_id()
        )
        db.session.add(order)
        db.session.commit()
    del session['cart_item']
    del session['all_total_quantity']
    del session['all_total_price']
    return render_template('entries/check_out.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name=form.name.data,
                email=form.email.data,
                address=form.address.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)  # Log in as newly created user
            return redirect(url_for("home_page"))
        flash('A user already exists with that email address.')
    return render_template('entries/signup.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for("home_page"))

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            # next_page = request.args.get("next")
            return redirect(url_for("home_page"))
        flash("無效的帳號或密碼")
        return redirect(url_for("login"))
    return render_template(
        "entries/login.html",
        form=form
    )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@login_manager.user_loader
def load_user(user_id):
    # Check if user is logged-in upon page load
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    # Redirect unauthorized users to Login page
    flash("You must be logged in to view that page.")
    return redirect(url_for("login"))
