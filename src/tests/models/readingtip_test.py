import unittest
from models.readingtip import ReadingTip

class TestReadingTip(unittest.TestCase):
    def test_constructor_sets_fields_correctly(self):
        readingtip = ReadingTip("Hyvä kirja", "https://kirjakauppa.fi/123")
        self.assertEqual(readingtip.title, "Hyvä kirja")
        self.assertEqual(readingtip.link, "https://kirjakauppa.fi/123")

    def test_constructor_adds_http(self):
        readingtip = ReadingTip("Keskinkertainen kirja", "kirjakauppa.fi/124")
        self.assertEqual(readingtip.link, "http://kirjakauppa.fi/124")

    def test_constructor_preserves_http(self):
        readingtip = ReadingTip("Huono kirja", "http://kirjakauppa.fi/125")
        self.assertEqual(readingtip.link, "http://kirjakauppa.fi/125")
