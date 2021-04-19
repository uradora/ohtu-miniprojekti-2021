from flask_login import login_user, logout_user

from repositories.user_repository import (user_repository as default_repository)

class UserService:
    def __init__(self, user_repository=default_repository):
        self._user_repository = user_repository

    def login(self, username, password):
        user = self._user_repository.check_login(username, password)
        if user is not None:
            login_user(user)
            return True
        else:
            return False

    def logout(self):
        logout_user()

    def register(self, username, password):
        if self._user_repository.register(username, password) is not None:
            return True
        return False

user_service = UserService()
