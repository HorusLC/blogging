from dao.jsonrepo import JsonRepository


class CommentRepository(JsonRepository):
    def fetch_by_post_id(self, post_id):
        return [comment for comment in self.find_all() if comment.post_id == post_id]

    def fetch_by_author_id(self, author_id):
        return [comment for comment in self.find_all() if comment.author_id == author_id]

    def fetch_by_post_author(self, post_id, author_id):
        return [comment for comment in self.find_all() if comment.post_id == post_id if comment.author_id == author_id]
