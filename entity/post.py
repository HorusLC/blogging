

class Post:

    def __init__(self, title, content, date_created, last_edited, tags, gallery, blog_: 'entity.blog.Blog',
                 comments: list['entity.comment.Comment'], id_=None):
        self.id_ = id_
        self.title = title
        self.content = content
        self.date_created = date_created
        self.last_edited = last_edited
        self.tags = tags
        self.gallery = gallery
        self.blog = blog_
        self.comments = comments

    def __str__(self):
        return ''.join(f'{self.title} - {self.date_created}')
