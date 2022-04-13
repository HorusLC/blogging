from Exceptions.entity_errors import EntityNotFoundError
from dao.blog_repo import BlogRepository
from dao.post_repo import PostRepository


class BlogManagementService:
    def __init__(self, blog_repo: BlogRepository, post_repo: PostRepository):
        self.blog_repo = blog_repo
        self.post_repo = post_repo

    def add_blog(self, blog, user_id):
        #self.blog_repo.load()
        blog.owner_id=user_id
        blog_created = self.blog_repo.create(blog)
        self.blog_repo.save()
        return blog_created

    def edit_blog_info(self, blog):
        self.blog_repo.load()
        self.blog_repo.update(blog)
        self.blog_repo.save()

    def delete_blog(self, blog):
        try:
            self.blog_repo.load()
            self.blog_repo.delete_by_id(blog.id_)
            for post in self.post_repo.find_all():
                if post.blog_id == blog.id_:
                    self.post_repo.delete_by_id(post.id_)

        except EntityNotFoundError as enfe:
            raise enfe

        else:
            self.blog_repo.save()
            self.post_repo.save()

    def fetch_user_blogs(self, blogger_id):
        self.blog_repo.load()
        return [blog for blog in self.blog_repo if blog.owner_id == blogger_id]

    def fetch_followed_blogs(self, user_id):
        # TODO implement this
        pass
