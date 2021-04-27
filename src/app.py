import os
from flask import Flask
from sqlalchemy.exc import SQLAlchemyError
from database import db
from login import login_manager

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

if os.environ.get("HEROKU"):
    app.secret_key = os.environ.get("SECRET_KEY")
    uri = os.environ.get("DATABASE_URL")
    # SQLAlchemy is picky about the protocol name, Heroku gives the wrong one.
    uri = uri.replace("postgres://", "postgresql://")
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
else:
    app.secret_key = b"\xb9>S-}k0f\x0e*\\*m\x9c\x00\xcd"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tips.db"
    #prints SQL-queries
    app.config["SQLALCHEMY_ECHO"] = True
    #browser reload will show template modifications
    app.config["TEMPLATES_AUTO_RELOAD"] = True


db.init_app(app)
login_manager.init_app(app)

import routes # pylint: disable=unused-import, wrong-import-position

with app.app_context():
    try:
        db.create_all()
    except SQLAlchemyError as exception:
        print(exception)
