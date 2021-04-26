import unittest
from services.readingtip_service import ReadingTipService
from models.user import User
from .login_service_stub import LoginServiceStub

class ReadingTipRepositoryStub:
    def __init__(self):
        tips = []
        self._tips = tips
        self._id_counter = 1

    def get_tips(self, user, tag):
        if tag == "all":
            return [t for t in self._tips if t.user == user]
        else:
            return [t for t in self._tips if t.user == user and tag in [tag.name for tag in t.tags]]

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

    def read_tip(self, tip_obj, date):
        for tip in self._tips:
            if tip.id == tip_obj.id:
                tip.read = date

    def contains_title(self, user, title):
        for readingtip in self.get_tips(user, "all"):
            if readingtip.title == title:
                return True
        return False

    def update_tip(self, tip_id, title, link, tags):
        for tip in self._tips:
            if tip.id == tip_id:
                tip.title = title
                tip.link = link
                tip.tags = tags

class TagRepositoryStub:
    def __init__(self):
        tags = []
        self._tags = tags
        self._id_counter = 1

    def get_tag(self, name):
        for tag in self._tags:
            if tag.name == name:
                return tag
        return None

    def create_tag(self, tag):
        tag.id = self._id_counter
        self._tags.append(tag)
        return tag

    def contains_tag(self, name):
        for tag in self._tags:
            if tag.name == name:
                return True
        return False



class TestReadingTipService(unittest.TestCase):
    def setUp(self):
        self.repository = ReadingTipRepositoryStub()
        self.tag_repository = TagRepositoryStub()
        self.login = LoginServiceStub()
        self.service = ReadingTipService(self.repository, self.login, self.tag_repository)
        self.user = User("maija", "yah2Oozo")
        self.user.id = 1
        self.login.login_user(self.user)

    def test_create_adds_to_collection(self):
        self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123", ["kirjat", "maksulliset"])
        self.service.create_tip("Huono kirja", "kirjakauppa.fi/124", ["kirjat", "maksulliset"])
        self.assertEqual(self.service.get_tips("all")[0].title, "Hyvä kirja")
        self.assertEqual(self.service.get_tips("all")[1].title, "Huono kirja")
        self.assertEqual(self.service.get_tips("all")[0].tags[0].name, "kirjat")
        self.assertEqual(self.service.get_tips("all")[0].tags[1].name, "maksulliset")

    def test_contains_title_if_not_present(self):
        assert not self.service.contains_title("Hyvä kirja")

    def test_contains_title_if_present(self):
        self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123", ["kirjat", "maksulliset"])
        assert self.service.contains_title("Hyvä kirja")

    def test_can_delete_own_tip(self):
        tip = self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123", ["kirjat", "maksulliset"])
        assert self.service.delete_tip(tip.id)
        assert not self.service.contains_title("Hyvä kirja")

    def test_cannot_delete_others_tip(self):
        other_user = User("mikko", "yah2Oozo")
        other_user.id = 2
        self.login.login_user(other_user)
        tip = self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123", ["kirjat", "maksulliset"])
        self.login.login_user(self.user)
        assert not self.service.delete_tip(tip.id)
        self.login.login_user(other_user)
        assert self.service.contains_title("Hyvä kirja")

    def test_can_get_tips_based_on_tags(self):
        self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123", ["hyvä"])
        self.service.create_tip("Huono kirja", "kirjakauppa.fi/124", ["huono"])
        self.assertEqual(len(self.service.get_tips("all")), 2)
        self.assertEqual(len(self.service.get_tips("hyvä")), 1)

    def test_returns_no_tips_if_no_user(self):
        self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123", ["hyvä"])
        self.service.create_tip("Huono kirja", "kirjakauppa.fi/124", ["huono"])
        self.login.logout_user()
        self.assertEqual(self.service.get_tips(), [])

    def test_can_change_own_tip(self):
        tip = self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123", ["kirjat", "maksulliset"])
        assert self.service.change_tip(tip, "Muutettu kirja", "kirjakauppa.fi/123", ["kirjat"])

    def test_tag_is_added_if_doesnt_exist(self):
        tip = self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123", ["kirjat", "maksulliset"])
        assert self.service.change_tip(tip, "Muutettu kirja", "kirjakauppa.fi/123", ["kalliit"])

    def test_cannot_change_others_tip(self):
        tip = self.service.create_tip("Maijan kirja", "kirjakauppa.fi/123", ["kirjat"])
        other_user = User("mikko", "yah2Oozo")
        other_user.id = 2
        self.login.login_user(other_user)
        assert not self.service.change_tip(tip, "Mikon kirja", "kirjakauppa.fi/123", ["maksulliset"])

    def test_can_get_one_tip(self):
        self.service.create_tip("Eka kirja", "ekakauppa.fi/123", ["kirjat"])
        self.service.create_tip("Toka kirja", "tokakauppa.fi/123", ["maksulliset"])
        tip = self.service.get_tip(2)
        assert tip.title == "Toka kirja"

    def test_can_read_own_tip(self):
        tip = self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123", ["kirjat", "maksulliset"])
        assert self.service.read_tip(tip.id)
        assert self.service.get_tips()[0].read is not None

    def test_cannot_read_others_tip(self):
        tip = self.service.create_tip("Maijan kirja", "kirjakauppa.fi/123", ["kirjat", "maksulliset"])
        other_user = User("mikko", "yah2Oozo")
        other_user.id = 2
        self.login.login_user(other_user)
        assert not self.service.read_tip(tip.id)

    def test_can_get_tag_names_from_own_tip(self):
        tip = self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123", ["kirjat", "maksulliset"])
        self.assertEqual(self.service.get_tag_names(tip), ["kirjat", "maksulliset"])

