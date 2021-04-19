from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
from database import db

class UserRepository:
    def __init__(self):
        pass

    def login(self, username, password):
        user = User.query.filter_by(username = username).first()
        if user is not None and user.check_password(request.form["password"]):
            login_user(user)
        return True

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
