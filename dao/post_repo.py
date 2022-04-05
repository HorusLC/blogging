from dao.jsonrepo import JsonRepository


class PostRepository(JsonRepository):

    def fetch_by_blog_id(self, blog_id):
        return [post for post in self.find_all() if post.blog_id == blog_id]
