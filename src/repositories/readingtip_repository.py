
class ReadingTipRepository:
    def __init__(self):
        # later use SQLAlchemy database session here
        # for now, just a list and some test data
        tips = []
        self._tips = tips

    def get_tips(self):
        return self._tips

    def create_tip(self, tip):
        self._tips.append(tip)

        return tip

    def contains_title(self, title):
        for readingtip in self.get_tips():
            if readingtip.title == title:
                return True
        return False

readingtip_repository = ReadingTipRepository()
