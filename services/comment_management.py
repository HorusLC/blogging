from dao.comment_repo import CommentRepository
from dao.post_repo import PostRepository


class CommentManagementService:
    def __init__(self, comment_repo: CommentRepository, post_repo: PostRepository):
        self.comment_repo = comment_repo
        self.post_repo = post_repo

    def refresh_context(self):
        self.comment_repo.load()
        self.post_repo.load()

    def add_comment(self, comment, author_id, post_id):
        self.comment_repo.load()
        created = self.comment_repo.create(comment)
        self.comment_repo.save()
        return created

    def fetch_post_comments(self, post_id):
        self.comment_repo.load()
        return [comment for comment in self.comment_repo.find_all() if comment.post_id == post_id]

    def delete_comment(self, comment):
        self.comment_repo.load()
        return self.comment_repo.delete_by_id(comment.id_)
