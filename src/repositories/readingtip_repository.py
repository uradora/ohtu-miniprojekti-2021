from models.readingtip import ReadingTip
from database import db

class ReadingTipRepository:
    def __init__(self):
        pass

    def get_tips(self, user, tag):
        if tag == "all":
            return ReadingTip.query.filter_by(user=user).all()
        else:
            return ReadingTip.query.filter_by(user=user).filter(ReadingTip.tags.any(name=tag)).all()

    def create_tip(self, tip):
        db.session.add(tip)
        db.session.commit()
        return tip

    def get_tip(self, tip_id):
        return ReadingTip.query.get(tip_id)

    def delete_tip(self, tip):
        db.session.delete(tip)
        db.session.commit()

    def contains_title(self, user, title):
        amount = ReadingTip.query.filter_by(user=user, title=title).count()
        return amount > 0

readingtip_repository = ReadingTipRepository()
