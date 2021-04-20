from database import db

class ReadingTip(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    link = db.Column(db.String(80), nullable = False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref=db.backref('tips', lazy=True))

    def __init__(self, title, link, owner, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        if not link.startswith("http://") and not link.startswith("https://"):
            link = "http://" + link
        self.link = link
        self.owner = owner
