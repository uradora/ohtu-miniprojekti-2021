from sqlalchemy.orm import validates
from database import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)

    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    @validates("name")
    def validate_name(self, _key, name):
        assert len(name) > 0, "Tag name must not be empty"
        assert len(name) <= 80, "Tag name is too long"
        return name
