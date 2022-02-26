from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('flask_cocoa.config')

db = SQLAlchemy(app)
#LOGIN CONFIGURATIONS####################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
#########################################

import flask_cocoa.views