import unittest
from models.readingtip import ReadingTip

class TestReadingTip(unittest.TestCase):
    def test_constructor_sets_fields_correctly(self):
        readingtip = ReadingTip("Hyvä kirja", "https://kirjakauppa.fi/123")
        self.assertEqual(readingtip.title, "Hyvä kirja")
        self.assertEqual(readingtip.link, "https://kirjakauppa.fi/123")
