from models.readingtip import ReadingTip
from models.tag import Tag
from login import (login_service as default_login_service)
from repositories.readingtip_repository import (readingtip_repository as default_repository)
from repositories.tag_repository import (tag_repository as default_tag_repository)

class ReadingTipService:
    def __init__(self, readingtip_repository=default_repository,
                 login_service=default_login_service,
                 tag_repository=default_tag_repository):
        self._readingtip_repository = readingtip_repository
        self._login_service = login_service
        self._tag_repository = tag_repository

    def get_tips(self, tag):
        if self._login_service.is_authenticated():
            return self._readingtip_repository.get_tips(self._login_service.current_user(), tag)
        else:
            return []

    def create_tip(self, title, link, tags):
        assert self._login_service.is_authenticated()
        readingTipTags = []
        for tag_name in tags:
            if not self._tag_repository.contains_tag(tag_name):
                self._tag_repository.create_tag(
                    Tag(tag_name)
                )
            readingTipTags.append(self._tag_repository.get_tag(tag_name))
        tip = self._readingtip_repository.create_tip(
            ReadingTip(title, link, self._login_service.current_user(), readingTipTags)
        )

        return tip

    def contains_title(self, title):
        assert self._login_service.is_authenticated()
        return self._readingtip_repository.contains_title(self._login_service.current_user(), title)

    def delete_tip(self, tip_id):
        assert self._login_service.is_authenticated()
        tip = self._readingtip_repository.get_tip(tip_id)
        if tip.user == self._login_service.current_user():
            self._readingtip_repository.delete_tip(tip)
            return True
        else:
            return False

readingtip_service = ReadingTipService()
