from models.readingtip import ReadingTip
from database import db

class ReadingTipRepository:
    def __init__(self):
        pass

    def get_tips(self, owner):
        return ReadingTip.query.filter_by(owner=owner).all()

    def create_tip(self, tip):
        db.session.add(tip)
        db.session.commit()
        return tip

    def contains_title(self, owner, title):
        amount = ReadingTip.query.filter_by(owner=owner, title=title).count()
        return amount > 0

readingtip_repository = ReadingTipRepository()
