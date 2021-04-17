import os
from flask import Flask
from sqlalchemy.exc import SQLAlchemyError
from database import db


app = Flask(__name__)

app.secret_key = "SECRET_KEY"


if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tips.db"
    #prints SQL-queries
    app.config["SQLALCHEMY_ECHO"] = True


db.init_app(app)


try:
    db.create_all()
except SQLAlchemyError:
    pass
