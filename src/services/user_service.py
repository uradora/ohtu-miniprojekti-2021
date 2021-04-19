from repositories.user_repository import (user_repository as default_repository)

class UserService:
    def __init__(self, user_repository=default_repository):
        self._user_repository = user_repository

    def login(self, username, password):
        return self._user_repository.login(username, password)

    def logout(self):
        self._user_repository.logout_user()

    def register(self, username, password):
        if self._user_repository.register(username, password) is not None:
            return True
        return False

user_service = UserService()
