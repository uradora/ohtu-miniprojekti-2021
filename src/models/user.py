from sqlalchemy.orm import validates
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from database import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False, unique = True)
    password_hash = db.Column(db.String())

    def __init__(self, username, password, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        assert len(password) > 0, "Password must not be empty"
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @validates("username")
    def validate_username(self, _key, username):
        assert len(username) > 0, "Username must not be empty"
        assert len(username) <= 80, "Username is too long"
        return username
