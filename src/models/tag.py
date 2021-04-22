from database import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)

    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name