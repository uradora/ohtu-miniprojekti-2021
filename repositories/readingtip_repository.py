from models.readingtip import ReadingTip

class ReadingTipRepository:
    def __init__(self):
        # later use SQLAlchemy database session here
        # for now, just a list and some test data
        tips = ["tip 1", "tip 2"]
        self._tips = tips

    def get_tips(self):
        return self._tips

    def create_tip(self, tip):
        self._tips.append(tip)

        return tip


        
