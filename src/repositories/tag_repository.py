from models.tag import Tag
from database import db

class TagRepository:
    def __init__(self):
        pass

    def get_tag(self, name):
        return Tag.query.filter_by(name=name).first()

    def get_tags(self, user=None):
        if user == None:
            return Tag.query.all()
        return Tag.query.filter(Tag.tips.any(user=user)).all()

    def create_tag(self, tag):
        db.session.add(tag)
        db.session.commit()
        return tag

    
    def contains_tag(self, name):
        amount = Tag.query.filter_by(name=name).count()
        return amount > 0

tag_repository = TagRepository()