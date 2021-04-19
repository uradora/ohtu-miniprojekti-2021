from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_login import current_user, login_user, logout_user

login = LoginManager()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False, unique = True)
    password_hash = db.Column(db.String())

    def __init__(self, username, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.username = username
        self.password_hash = generate_password_hash(password)

    def set_password(self, password):
        return check_password_hash(self.password_hash, password)

    def check_password(self, password):
        return check_password_hash(self.password_hash)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))