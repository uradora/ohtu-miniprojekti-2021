import unittest
from services.readingtip_service import ReadingTipService
from models.user import User
from .login_service_stub import LoginServiceStub

class ReadingTipRepositoryStub:
    def __init__(self):
        tips = []
        self._tips = tips
        self._id_counter = 1

    def get_tips(self, user):
        return [t for t in self._tips if t.user == user]

    def get_tip(self, tip_id):
        for tip in self._tips:
            if tip.id == tip_id:
                return tip
        return None

    def create_tip(self, tip):
        tip.id = self._id_counter
        self._id_counter += 1
        self._tips.append(tip)
        return tip

    def delete_tip(self, tip):
        self._tips = [t for t in self._tips if t != tip]

    def contains_title(self, user, title):
        for readingtip in self.get_tips(user):
            if readingtip.title == title:
                return True
        return False


class TestReadingTipService(unittest.TestCase):
    def setUp(self):
        self.repository = ReadingTipRepositoryStub()
        self.login = LoginServiceStub()
        self.service = ReadingTipService(self.repository, self.login)
        self.user = User("maija", "yah2Oozo")
        self.user.id = 1
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

    def test_can_delete_own_tip(self):
        tip = self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123")
        assert self.service.delete_tip(tip.id)
        assert not self.service.contains_title("Hyvä kirja")

    def test_cannot_delete_others_tip(self):
        other_user = User("mikko", "yah2Oozo")
        other_user.id = 2
        self.login.login_user(other_user)
        tip = self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123")
        self.login.login_user(self.user)
        assert not self.service.delete_tip(tip.id)
        self.login.login_user(other_user)
        assert self.service.contains_title("Hyvä kirja")
