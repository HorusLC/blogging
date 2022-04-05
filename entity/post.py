class Post:

    def __init__(self, title=None, content=None, date_created=None, last_edited=None, tags=None, gallery=None,
                 blog_id=None,
                 comments=None, id_=None):
        self.id_ = id_
        self.title = title
        self.content = content
        self.date_created = date_created
        self.last_edited = last_edited
        self.tags = tags
        self.gallery = gallery
        self.blog_id = blog_id
        self.comments = comments
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__

    def __str__(self):
        return ''.join(f'{self.title} - {self.date_created}')
