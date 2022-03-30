from entities.post import Post
from entities.user import User


class Comment:
    def __init__(self, id_, text, date_created, post: Post, author: User):
        self.id_ = id_
        self.text = text
        self.date_created = date_created
        self.post = post
        self.author = author

    def __str__(self):
        return "".join(f"{self.author.username} on {self.date_created}")
