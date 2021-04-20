import unittest
from services.readingtip_service import ReadingTipService
from models.user import User
from .login_service_stub import LoginServiceStub

class ReadingTipRepositoryStub:
    def __init__(self):
        tips = []
        self._tips = tips

    def get_tips(self, user):
        return [t for t in self._tips if t.user == user]

    def create_tip(self, tip):
        self._tips.append(tip)

        return tip

    def contains_title(self, user, title):
        for readingtip in self.get_tips(user):
            if readingtip.title == title:
                return True
        return False


class TestReadingTip(unittest.TestCase):
    def setUp(self):
        self.repository = ReadingTipRepositoryStub()
        self.login = LoginServiceStub()
        self.service = ReadingTipService(self.repository, self.login)
        self.user = User("maija", "yah2Oozo")
        self.login.login_user(self.user)

    def test_create_adds_to_collection(self):
        self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123")
        self.service.create_tip("Huono kirja", "kirjakauppa.fi/124")
        self.assertEqual(self.service.get_tips()[0].title, "Hyvä kirja")
        self.assertEqual(self.service.get_tips()[1].title, "Huono kirja")

    def test_contains_title_if_not_present(self):
        assert not self.service.contains_title("Hyvä kirja")

    def test_contains_title_if_present(self):
        self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123")
        assert self.service.contains_title("Hyvä kirja")
