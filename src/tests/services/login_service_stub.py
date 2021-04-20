
class LoginServiceStub:
    def __init__(self):
        self._user = None

    def login_user(self, user):
        self._user = user

    def logout_user(self):
        self._user = None

    def is_authenticated(self):
        return self._user is not None

    def current_user(self):
        assert self.is_authenticated()
        return self._user
