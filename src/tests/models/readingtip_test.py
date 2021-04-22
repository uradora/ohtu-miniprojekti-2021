import unittest
from models.readingtip import ReadingTip
from models.user import User

class TestReadingTip(unittest.TestCase):
    def setUp(self):
        self.user = User("maija", "jahph5Ie")

    def test_constructor_sets_fields_correctly(self):
        readingtip = ReadingTip("Hyvä kirja", "https://kirjakauppa.fi/123", self.user)
        self.assertEqual(readingtip.title, "Hyvä kirja")
        self.assertEqual(readingtip.link, "https://kirjakauppa.fi/123")

    def test_constructor_adds_http(self):
        readingtip = ReadingTip("Keskinkertainen kirja", "kirjakauppa.fi/124", self.user)
        self.assertEqual(readingtip.link, "http://kirjakauppa.fi/124")

    def test_constructor_preserves_http(self):
        readingtip = ReadingTip("Huono kirja", "http://kirjakauppa.fi/125", self.user)
        self.assertEqual(readingtip.link, "http://kirjakauppa.fi/125")
