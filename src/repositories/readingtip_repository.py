from models.readingtip import ReadingTip
from database import db

class ReadingTipRepository:
    def __init__(self):
        pass

    def get_tips(self):
        return ReadingTip.query.all()

    def create_tip(self, tip):
        db.session.add(tip)
        db.session.commit()
        return tip

    def contains_title(self, title):
        amount = ReadingTip.query.filter(ReadingTip.title == title).count()
        return amount > 0

readingtip_repository = ReadingTipRepository()
