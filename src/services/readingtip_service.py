from models.readingtip import ReadingTip
from repositories.readingtip_repository import (readingtip_repository as default_repository)

class ReadingTipService:
    def __init__(self, readingtip_repository=default_repository):
        self._readingtip_repository = readingtip_repository

    def get_tips(self):
        return self._readingtip_repository.get_tips()

    def create_tip(self, title, link):
        tip = self._readingtip_repository.create_tip(
            ReadingTip(title, link)
        )

        return tip

readingtip_service = ReadingTipService()



    