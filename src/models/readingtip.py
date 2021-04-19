from database import db

class ReadingTip(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    link = db.Column(db.String(80), nullable = False)

    def __init__(self, title, link, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        if not link.startswith("http://") and not link.startswith("https://"):
            link = "http://" + link
        self.link = link
