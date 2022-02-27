from flask_script import Command
from flask_cocoa import db
from flask_cocoa.models.entries import User, Order


class InitDB(Command):
    # create table
    def run(self):
        db.create_all()