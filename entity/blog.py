
class Blog:

    def __init__(self, title, description, date_created, last_posted, tags, category, total_follows,
                 owner: 'Blogger', posts: list['Post'] = None, id_=None):
        self.id_ = id_
        self.title = title
        self.description = description
        self.date_created = date_created
        self.last_posted = last_posted
        self.tags = tags
        self.category = category
        self.total_follows = total_follows
        self.owner = owner
        self.posts = posts

    def __str__(self):
        return "".join(f"{self.owner.username}'s {self.title}")
