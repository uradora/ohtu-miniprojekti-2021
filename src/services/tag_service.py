from login import (login_service as default_login_service)
from repositories.tag_repository import (tag_repository as default_tag_repository)

class TagService:
    def __init__(self, login_service=default_login_service,
                 tag_repository=default_tag_repository):
        self._login_service = login_service
        self._tag_repository = tag_repository

    def get_tags(self):
        if self._login_service.is_authenticated():
            return self._tag_repository.get_tags(self._login_service.current_user())
        else:
            return []

tag_service = TagService()