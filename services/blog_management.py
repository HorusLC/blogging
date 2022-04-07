from dao.blog_repo import BlogRepository


class BlogManagementService:
    def __init__(self, blog_repo: BlogRepository):
        self.blog_repo = blog_repo

    def add_blog(self, blog, user_id):
        self.blog_repo.load()
        blog_created = self.blog_repo.create(blog)
        self.blog_repo.save()
        return blog_created

    def edit_blog_info(self, blog):
        self.blog_repo.load()
        self.blog_repo.update(blog)
        self.blog_repo.save()

    def delete_blog(self, blog):
        self.blog_repo.load()
        self.blog_repo.delete_by_id(blog.id_)
        self.blog_repo.save()

    def fetch_user_blogs(self, blogger_id):
        self.blog_repo.load()
        return [blog for blog in self.blog_repo if blog.owner_id == blogger_id]

    def fetch_followed_blogs(self, user_id):
        # TODO implement this
        pass
