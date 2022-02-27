from flask import request, redirect, url_for, render_template, flash, session
from flask_cocoa import app
from flask_cocoa import db
from flask_cocoa.forms import SignupForm, LoginForm
from flask_cocoa.models.entries import Product, User
from flask_login import current_user, login_user, login_required, logout_user
from flask_cocoa import login_manager


@app.route('/')
def home_page():
    data = Product.query.all()
    return render_template('entries/index.html', data=data)


@app.route('/<product_ID>')
def show_item(product_ID):
    item = Product.query.filter_by(product_ID=product_ID).first()
    data = Product.query.all()[:4]
    return render_template('entries/product.html', item=item, data=data)


@app.route('/product_list')
def show_entries():
    items = Product.query.all()
    return render_template('entries/product_list.html', items=items)


@app.route('/hot_list')
def show_hot():
    items = Product.query.all()[:5]
    return render_template('entries/hot_list.html', items=items)


@app.route('/shopping_cart')
def show_shopping_cart():
    items = Product.query.all()[:5]
    return render_template('entries/shopping_cart.html', items=items)

@app.route('/add_cart', methods=["POST"])
def add_cart():
    if 'cart_item' not in session:
        session['cart_item'] = 0
    session['cart_item'] += int(request.form['quantity'])
    return redirect(request.referrer)



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
