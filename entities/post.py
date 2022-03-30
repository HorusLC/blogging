from entities.blog import Blog
from entities.comment import Comment


class Post:

    def __init__(self, id_, title, content, date_created, last_edited, tags, gallery, blog: Blog,
                 comments: list[Comment]):
        self.id_ = id_
        self.title = title
        self.content = content
        self.date_created = date_created
        self.last_edited = last_edited
        self.tags = tags
        self.gallery = gallery
        self.blog = blog
        self.comments = comments

    def __str__(self):
        return ''.join(f'{self.title} - {self.date_created}')
