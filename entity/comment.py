class Comment:
    def __init__(self, text=None, date_created=None, post_id: str = None, author_id=None, id_=None):
        self.id_ = id_
        self.text = text
        self.date_created = date_created
        self.post_id = post_id
        self.author_id = author_id
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__

    def __str__(self):
        return self.text
