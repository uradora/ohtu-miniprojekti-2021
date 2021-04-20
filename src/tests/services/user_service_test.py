import unittest
from services.user_service import UserService
from models.user import User
from .login_service_stub import LoginServiceStub

class UserRepositoryStub:
    def __init__(self):
        self._users = []

    def check_login(self, username, password):
        for user in self._users:
            if user.username == username:
                if user.check_password(password):
                    return user
                else:
                    return None
        return None

    def register(self, username, password):
        for user in self._users:
            if user.username == username:
                return None
        user = User(username=username, password=password)
        self._users.append(user)
        return user


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.repository = UserRepositoryStub()
        self.login = LoginServiceStub()
        self.service = UserService(self.repository, self.login)
        self.service.register("maija", "yue3AeV4")

    def test_register_new_username(self):
        result = self.service.register("mikko", "yue3AeV4")
        assert result

    def test_register_existing_username(self):
        result = self.service.register("maija", "salasana123")
        assert not result

    def test_correct_login_sets_session(self):
        result = self.service.login("maija", "yue3AeV4")
        assert result
        assert self.login.is_authenticated()

    def test_incorrect_password_does_not_set_session(self):
        result = self.service.login("maija", "yue3AeV")
        assert not result
        assert not self.login.is_authenticated()

    def test_logout_unsets_session(self):
        self.service.login("maija", "yue3AeV4")
        self.service.logout()
        assert not self.login.is_authenticated()
