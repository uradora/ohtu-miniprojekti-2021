from models.readingtip import ReadingTip
from database import db

class ReadingTipRepository:
    def __init__(self):
        pass

    def get_tips(self, user, tag="all"):
        if tag == "all":
            return ReadingTip.query.filter_by(user=user).all()
        else:
            return ReadingTip.query.filter_by(user=user).filter(ReadingTip.tags.any(name=tag)).all()

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

    def read_tip(self, tip, date):
        ReadingTip.query.filter_by(id=tip.id).update({"read":date})
        db.session.commit()

readingtip_repository = ReadingTipRepository()
