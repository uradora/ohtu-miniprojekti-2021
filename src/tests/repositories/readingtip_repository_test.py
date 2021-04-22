import unittest
from repositories.readingtip_repository import ReadingTipRepository
from repositories.user_repository import UserRepository
from models.readingtip import ReadingTip
from models.tag import Tag

class TestReadingTip(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository()
        self.user = self.user_repository.register("maija", "Tiothee6")
        self.repository = ReadingTipRepository()
        

    def test_create_tip(self):
        tags = [Tag("kirjat"), Tag("maksulliset")]
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", self.user, tags))
        tips = self.repository.get_tips(self.user, "all")
        self.assertEqual(tips[0].title, "Hyvä kirja")
        self.assertEqual(tips[0].tags[0].name, "kirjat")
        self.assertEqual(tips[0].tags[1].name, "maksulliset")

    def test_contains_title_if_not_present(self):
        tags = [Tag("kirjat"), Tag("maksulliset")]
        assert not self.repository.contains_title(self.user, "Hyvä kirja")

    def test_contains_title_if_present(self):
        tags = [Tag("kirjat"), Tag("maksulliset")]
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", self.user, tags))
        assert self.repository.contains_title(self.user, "Hyvä kirja")

    def test_deletes_tip(self):
        tags = [Tag("kirjat"), Tag("maksulliset")]
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", self.user, tags))
        tip = self.repository.get_tips(self.user, "all")[0]
        self.repository.delete_tip(tip)
        self.assertEqual(self.repository.get_tips(self.user, "all"), [])

    def test_cannot_see_others_tip(self):
        tags = [Tag("kirjat"), Tag("maksulliset")]
        second_user = self.user_repository.register("mikko", "oko7Aeko")
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", second_user, tags))

        assert not self.repository.contains_title(self.user, "Hyvä kirja")
        self.assertEqual(self.repository.get_tips(self.user, "all"), [])

    def test_can_get_tips_based_on_tags(self):
        tags = [Tag("Hyvä")]
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", self.user, tags))
        secondTags = [Tag("Huono")]
        self.repository.create_tip(ReadingTip("Huono kirja", "kirjakauppa.fi/123", self.user, secondTags))
        self.assertEqual(len(self.repository.get_tips(self.user, "all")), 2)
        self.assertEqual(len(self.repository.get_tips(self.user, "Hyvä")), 1)


