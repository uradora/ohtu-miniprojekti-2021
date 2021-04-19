import unittest
from werkzeug.security import check_password_hash
from models.user import User

class TestUser(unittest.TestCase):
    def test_constructor_sets_fields_correctly(self):
        user = User("maija", "Ahlie8oh")
        self.assertEqual(user.username, "maija")
        assert check_password_hash(user.password_hash, "Ahlie8oh")

    def test_set_password_updates_password_hash(self):
        user = User("maija", "Ahlie8oh")
        user.set_password("Ahlie8ohe")
        assert check_password_hash(user.password_hash, "Ahlie8ohe")

    def test_check_password_correct(self):
        user = User("maija", "Ahlie8oh")
        assert user.check_password("Ahlie8oh")

    def test_check_password_incorrect(self):
        user = User("maija", "Ahlie8oh")
        assert not user.check_password("ahlie8oh")
