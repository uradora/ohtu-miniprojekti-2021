import unittest
from services.readingtip_service import ReadingTipService

class ReadingTipRepositoryStub:
    def __init__(self):
        tips = []
        self._tips = tips

    def get_tips(self):
        return self._tips

    def create_tip(self, tip):
        self._tips.append(tip)

        return tip

    def contains_title(self, title):
        for readingtip in self.get_tips():
            if readingtip.title == title:
                return True
        return False


class TestReadingTip(unittest.TestCase):
    def setUp(self):
        self.repository = ReadingTipRepositoryStub()
        self.service = ReadingTipService(self.repository)

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
