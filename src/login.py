from flask_login import LoginManager, login_user, logout_user, current_user
from models.user import User

login_manager = LoginManager()
class LoginService:
    def login_user(self, user):
        login_user(user)

    def logout_user(self):
        logout_user()

    def is_authenticated(self):
        return current_user.is_authenticated

    def current_user(self):
        return current_user

login_service = LoginService()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
