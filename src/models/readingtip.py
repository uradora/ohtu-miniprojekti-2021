from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from database import db

tips_to_tags_table = db.Table("tipsToTagsTable",
    db.Column("tip_id", db.Integer, db.ForeignKey("reading_tip.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"))
)

class ReadingTip(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    _link = db.Column("link", db.String(120), nullable = False)
    read = db.Column(db.String(20), nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('tips', lazy=True))
    tags = db.relationship("Tag", secondary = tips_to_tags_table, backref=db.backref("tips"))

    def __init__(self, title, link, user, tags, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.link = link
        self.user = user
        self.tags = tags

    @hybrid_property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        if not link.startswith("http://") and not link.startswith("https://"):
            link = "http://" + link
        self._link = link

    @validates("title")
    def validate_title(self, _key, title):
        assert len(title) > 0, "Title must not be empty"
        assert len(title) <= 80, "Title is too long"
        return title

    @validates("_link")
    def validate_link(self, _key, link):
        if link.startswith("http://"):
            assert len(link) > len("http://"), "Link must not be empty"
        elif link.startswith("https://"):
            assert len(link) > len("https://"), "Link must not be empty"
        else:
            raise AssertionError("Link must start with protocol")
        assert len(link) <= 120, "Link is too long"
        return link
