
class Blog:

    def __init__(self, title=None, description=None, date_created=None, last_posted=None, tags=None, category=None,
                 owner_id = None, id_=None):
        self.id_ = id_
        self.title = title
        self.description = description
        self.date_created = date_created
        self.last_posted = last_posted
        self.tags = tags
        self.category = category
        self.owner_id = owner_id
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__

    def __str__(self):
        return self.title
