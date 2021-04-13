class ReadingTip:
    def __init__(self, title, link):
        self.title = title
        if not link.startswith("http://") and not link.startswith("https://"):
            link = "http://" + link
        self.link = link
