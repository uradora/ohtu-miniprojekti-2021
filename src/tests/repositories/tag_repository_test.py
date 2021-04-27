import unittest
from repositories.tag_repository import TagRepository
from models.tag import Tag

class TestTag(unittest.TestCase):
    def setUp(self):
        self.repository = TagRepository()

    def test_create_tag(self):
        self.repository.create_tag(Tag("kirjat"))
        tags = self.repository.get_tags()
        self.assertEqual(tags[0].name, "kirjat")

    def test_contains_tag_if_not_present(self):
        assert not self.repository.contains_tag("kirjat")

    def test_contains_tag_if_present(self):
        self.repository.create_tag(Tag("kirjat"))
        assert self.repository.contains_tag("kirjat")
