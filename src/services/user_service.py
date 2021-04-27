from login import (login_service as default_login_service)
from repositories.user_repository import (user_repository as default_repository)

class UserService:
    def __init__(self, user_repository=default_repository, login_service=default_login_service):
        self._user_repository = user_repository
        self._login_service = login_service

    def login(self, username, password):
        user = self._user_repository.check_login(username, password)
        if user is not None:
            self._login_service.login_user(user)
            return True
        else:
            return False

    def logout(self):
        self._login_service.logout_user()

    def register(self, username, password):
        assert not self._user_repository.contains_username(username), "Username is taken"
        self._user_repository.register(username, password)
        self.login(username, password)

    def is_authenticated(self):
        return self._login_service.is_authenticated()

user_service = UserService()
