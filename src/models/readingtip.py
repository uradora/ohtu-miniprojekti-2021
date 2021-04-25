from database import db
from models.tag import Tag


tips_to_tags_table = db.Table("tipsToTagsTable",
    db.Column("tip_id", db.Integer, db.ForeignKey("reading_tip.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"))
)


class ReadingTip(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    link = db.Column(db.String(80), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('tips', lazy=True))
    tags = db.relationship("Tag", secondary = tips_to_tags_table, backref=db.backref("tips"))

    def __init__(self, title, link, user, tags,  **kwargs):
        super().__init__(**kwargs)
        self.title = title
        if not link.startswith("http://") and not link.startswith("https://"):
            link = "http://" + link
        self.link = link
        self.user = user
        self.tags = tags
