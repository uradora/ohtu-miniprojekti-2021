from models.tag import Tag
from database import db

class TagRepository:
    def __init__(self):
        pass

    def get_tags(self):
        return Tag.query.all()

    def create_tag(self, tag):
        db.session.add(tag)
        db.session.commit()
        return tag

    
    def contains_tag(self, name):
        amount = Tag.query.filter_by(name=name).count()
        return amount > 0

tag_repository = TagRepository()