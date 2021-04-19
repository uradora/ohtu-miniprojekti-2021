from models.user import User
from database import db
from flask_login import LoginManager
from flask_login import login_user, logout_user

login = LoginManager()

class UserRepository:
    def __init__(self):
        pass

    def login(self, username, password):
        user = User.query.filter_by(username = username).first()
        if user is not None and user.check_password(password):
            login_user(user)
            return True
        return False

    def logout(self):
        logout_user()

    def register(self, username, password):
        if User.query.filter_by(username=username).first():
            return None
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user


user_repository = UserRepository()
