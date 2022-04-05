from dao.jsonrepo import JsonRepository
from dao.repository_base import Repository
from entity.user import User


class BloggerRepository(JsonRepository):

    def find_by_email(self, email):
        return next(filter(lambda u: u.email == email, self.find_all()), None)

    def find_by_username(self, username):
        return next(filter(lambda u: u.username == username, self.find_all()), None)


