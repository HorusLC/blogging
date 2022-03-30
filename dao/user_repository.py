from dao.repository_base import Repository
from entity.user import User


class UserRepository(Repository):

    def find_by_email(self, email):
        return next(filter(lambda u: u.email == email, self._entities.values()), None)

    def find_by_username(self, username):
        return next(filter(lambda u: u.username == username, self._entities.values()), None)

