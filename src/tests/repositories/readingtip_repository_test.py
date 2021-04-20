import unittest
from repositories.readingtip_repository import ReadingTipRepository
from repositories.user_repository import UserRepository
from models.readingtip import ReadingTip

class TestReadingTip(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository()
        self.user = self.user_repository.register("maija", "Tiothee6")
        self.repository = ReadingTipRepository()

    def test_create_tip(self):
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", self.user))
        tips = self.repository.get_tips(self.user)
        self.assertEqual(tips[0].title, "Hyvä kirja")

    def test_contains_title_if_not_present(self):
        assert not self.repository.contains_title(self.user, "Hyvä kirja")

    def test_contains_title_if_present(self):
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", self.user))
        assert self.repository.contains_title(self.user, "Hyvä kirja")

    def test_deletes_tip(self):
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", self.user))
        tip = self.repository.get_tips(self.user)[0]
        self.repository.delete_tip(tip)
        self.assertEqual(self.repository.get_tips(self.user), [])

    def test_cannot_see_others_tip(self):
        second_user = self.user_repository.register("mikko", "oko7Aeko")
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", second_user))

        assert not self.repository.contains_title(self.user, "Hyvä kirja")
        self.assertEqual(self.repository.get_tips(self.user), [])
