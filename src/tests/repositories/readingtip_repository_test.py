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
        tips = self.repository.get_tips(self.user)
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
        tip = self.repository.get_tips(self.user)[0]
        self.repository.delete_tip(tip)
        self.assertEqual(self.repository.get_tips(self.user), [])

    def test_cannot_see_others_tip(self):
        tags = [Tag("kirjat"), Tag("maksulliset")]
        second_user = self.user_repository.register("mikko", "oko7Aeko")
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", second_user, tags))

        assert not self.repository.contains_title(self.user, "Hyvä kirja")
        self.assertEqual(self.repository.get_tips(self.user), [])

    def test_update_tip(self):
        tags = [Tag("kirjat"), Tag("maksulliset")]
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", self.user, tags))
        tags.append(Tag("uusi"))
        self.repository.update_tip(1, "Muutettu kirja", "kirjakauppa.fi/123", tags)
        self.assertEqual(self.repository.get_tips(self.user)[0].title, "Muutettu kirja")
        self.assertEqual(self.repository.get_tips(self.user)[0].tags[2].name, "uusi")

    def test_get_tip(self):
        tags = [Tag("kirjat"), Tag("maksulliset")]
        self.repository.create_tip(ReadingTip("Uusi kirja", "kirjakauppa.fi/123", self.user, tags))
        tip = self.repository.get_tip(1)
        self.assertEqual(tip.title, "Uusi kirja")

    def test_marks_tip_as_read(self):
        tags = [Tag("kirjat"), Tag("maksulliset")]
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123", self.user, tags))
        assert self.repository.get_tips(self.user)[0].read is None
        self.repository.read_tip(self.repository.get_tips(self.user)[0], "2021")
        assert self.repository.get_tips(self.user)[0].read is not None
