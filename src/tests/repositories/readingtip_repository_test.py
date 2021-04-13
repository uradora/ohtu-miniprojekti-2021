import unittest
from repositories.readingtip_repository import ReadingTipRepository
from models.readingtip import ReadingTip

class TestReadingTip(unittest.TestCase):
    def setUp(self):
        self.repository = ReadingTipRepository()

    def test_create_tip(self):
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123"))
        self.assertEqual(self.repository.get_tips()[0].title, "Hyvä kirja")

    def test_contains_title_if_not_present(self):
        assert not self.repository.contains_title("Hyvä kirja")

    def test_contains_title_if_present(self):
        self.repository.create_tip(ReadingTip("Hyvä kirja", "kirjakauppa.fi/123"))
        assert self.repository.contains_title("Hyvä kirja")
