from models.user import User
from database import db

class UserRepository:
    def __init__(self):
        pass

    def check_login(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            return user
        else:
            return None

    def register(self, username, password):
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def contains_username(self, username):
        return bool(User.query.filter_by(username=username).first())

user_repository = UserRepository()
