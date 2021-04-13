import unittest
from services.readingtip_service import ReadingTipService
from repositories.readingtip_repository import ReadingTipRepository

class TestReadingTip(unittest.TestCase):
    def setUp(self):
        self.repository = ReadingTipRepository()
        self.service = ReadingTipService(self.repository)

    def test_create_adds_to_collection(self):
        self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123")
        self.service.create_tip("Huono kirja", "kirjakauppa.fi/124")
        self.assertEqual(self.service.get_tips()[0].title, "Hyvä kirja")
        self.assertEqual(self.service.get_tips()[1].title, "Huono kirja")

    def test_contains_title_if_not_present(self):
        assert not self.service.containsTitle("Hyvä kirja")

    def test_contains_title_if_present(self):
        self.service.create_tip("Hyvä kirja", "kirjakauppa.fi/123")
        assert self.service.containsTitle("Hyvä kirja")
