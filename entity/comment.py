
class Comment:
    def __init__(self, text, date_created, post_: 'entity.post.Post', author: 'entity.user.User', id_=None):
        self.id_ = id_
        self.text = text
        self.date_created = date_created
        self.post = post_
        self.author = author

    def __str__(self):
        return "".join(f"{self.author.username} on {self.date_created}")
