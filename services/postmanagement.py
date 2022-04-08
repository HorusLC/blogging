from Exceptions.entity_errors import EntityNotFoundError
from dao.post_repo import PostRepository
from dao.comment_repo import CommentRepository


class PostManagementService:
    def __init__(self, post_repo: PostRepository, comment_repo: CommentRepository):
        self.post_repo = post_repo
        self.comment_repo = comment_repo

    def add_post_to_blog(self, post, blog_id):
        self.post_repo.load()
        self.post_repo.create(post)
        self.post_repo.save()
        return post

    def edit_post(self, post):
        self.post_repo.load()
        self.post_repo.update(post)
        self.post_repo.save()
        return post

    def delete_post(self, post):
        try:
            self.post_repo.load()
            self.comment_repo.load()
            self.post_repo.delete_by_id(post.id_)
            comment_ids = [comment.id_ for comment in self.comment_repo.find_all() if comment.post_id == post.id_]
            for id_ in comment_ids:
                self.comment_repo.delete_by_id(id_)
        except EntityNotFoundError as enfe:
            raise enfe
        else:
            self.post_repo.save()
            self.comment_repo.save()

        return post

