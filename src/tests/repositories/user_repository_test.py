import unittest
from repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repository = UserRepository()
        self.repository.register("maija", "Ahlie8oh")

    def test_register_user(self):
        user = self.repository.register("matti", "salasana123")
        assert user is not None

    def test_register_user_existing_username(self):
        user = self.repository.register("maija", "salasana123")
        assert user is None

    def test_check_login_correct(self):
        result = self.repository.check_login("maija", "Ahlie8oh")
        self.assertEqual(result.username, "maija")

    def test_check_login_incorrect_password(self):
        result = self.repository.check_login("maija", "Ahlie8ohe")
        assert result is None

    def test_check_login_incorrect_username(self):
        result = self.repository.check_login("maije", "Ahlie8oh")
        assert result is None
