from flask_login import current_user # refactor out later
from models.readingtip import ReadingTip
from repositories.readingtip_repository import (readingtip_repository as default_repository)

class ReadingTipService:
    def __init__(self, readingtip_repository=default_repository):
        self._readingtip_repository = readingtip_repository

    def get_tips(self):
        assert current_user.is_authenticated
        return self._readingtip_repository.get_tips(current_user)

    def create_tip(self, title, link):
        assert current_user.is_authenticated
        tip = self._readingtip_repository.create_tip(
            ReadingTip(title, link, current_user)
        )
        return tip

    def contains_title(self, title):
        assert current_user.is_authenticated
        return self._readingtip_repository.contains_title(current_user, title)

readingtip_service = ReadingTipService()
