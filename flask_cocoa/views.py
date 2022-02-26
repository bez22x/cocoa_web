from flask import request, redirect, url_for, render_template, flash, session
from flask_cocoa import app
from flask_cocoa import db
# from flask_cocoa.forms import SignupForm
from flask_cocoa.models.entries import Product


@app.route('/')
def home_page():
	data = Product.query.all()
	return render_template('entries/index.html',data=data)

@app.route('/<product_ID>')
def show_item(product_ID):
	item = Product.query.filter_by(product_ID=product_ID).first()
	data = Product.query.all()[:4]
	return render_template('entries/product.html', item=item, data=data)

@app.route('/product_list')
def show_entries():
	items = Product.query.all()
	return render_template('entries/product_list.html',items=items)

@app.route('/hot_list')
def show_hot():
	items = Product.query.all()[:5]
	return render_template('entries/hot_list.html',items=items)

@app.route('/shopping_car')
def show_shoping_car():
	return 'no post'

# @app.route('/signup', methods=["GET", "POST"])
# def signup():
#     form = SignupForm()
#     if form.validate_on_submit():
#         existing_user = User.query.filter_by(email=form.email.data).first()
#         if existing_user is None:
#             user = User(
#                 name=form.name.data, email=form.email.data, website=form.website.data
#             )
#             user.set_password(form.password.data)
#             db.session.add(user)
#             db.session.commit()  # Create new user
#             login_user(user)  # Log in as newly created user
#             return redirect(url_for("main_bp.dashboard"))
#         flash("A user already exists with that email address.")
#     return render_template(
#         "signup.jinja2",
#         title="Create an Account.",
#         form=form,
#         template="signup-page",
#         body="Sign up for a user account.",
#     )
#
#
# @auth_bp.route("/login", methods=["GET", "POST"])
# def login():
#     """
#     Log-in page for registered users.
#     GET requests serve Log-in page.
#     POST requests validate and redirect user to dashboard.
#     """
#     # Bypass if user is logged in
#     if current_user.is_authenticated:
#         return redirect(url_for("main_bp.dashboard"))
#
#     form = LoginForm()
#     # Validate login attempt
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and user.check_password(password=form.password.data):
#             login_user(user)
#             next_page = request.args.get("next")
#             return redirect(next_page or url_for("main_bp.dashboard"))
#         flash("Invalid username/password combination")
#         return redirect(url_for("auth_bp.login"))
#     return render_template(
#         "login.jinja2",
#         form=form,
#         title="Log in.",
#         template="login-page",
#         body="Log in with your User account.",
#     )
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     """Check if user is logged-in upon page load."""
#     if user_id is not None:
#         return User.query.get(user_id)
#     return None
#
#
# @login_manager.unauthorized_handler
# def unauthorized():
#     """Redirect unauthorized users to Login page."""
#     flash("You must be logged in to view that page.")
#     return redirect(url_for("auth_bp.login"))

