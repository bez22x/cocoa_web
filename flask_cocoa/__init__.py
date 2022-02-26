from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('flask_cocoa.config')

db = SQLAlchemy(app)
# bootstrap = Bootstrap(app)

import flask_cocoa.views