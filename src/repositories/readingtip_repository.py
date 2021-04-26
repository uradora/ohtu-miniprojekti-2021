from models.readingtip import ReadingTip
from database import db

class ReadingTipRepository:
    def __init__(self):
        pass

    def get_tips(self, user):
        return ReadingTip.query.filter_by(user=user).all()

    def update_tip(self, tip_id, title, link, tags):
        tip = self.get_tip(tip_id)
        print(tags)
        tip.title = title
        tip.link = link
        tip.tags = tags
        db.session.commit()

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
