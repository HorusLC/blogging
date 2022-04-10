from Exceptions.usererror import UsernameNotFoundError, IncorrectPasswordError, EmailNotFoundError
from dao.blogger_repository import BloggerRepository
from entity.blogger import Blogger
from services.phasher import PassHasher
from datetime import datetime as dt
from datetime import date


class Login:
    def __init__(self, hasher: PassHasher, blogger_repo: BloggerRepository):
        self.hasher = hasher
        self.blogger_repo = blogger_repo

    def try_login_email(self, email, password):
        self.blogger_repo.load()  # not sure if we should refresh here, or in the find_by_uname() repo function
        user_found: Blogger = self.blogger_repo.find_by_email(email)
        if user_found is None:
            raise EmailNotFoundError(f'No such email: {email} found!')
        if not self.hasher.check_pass(bytes.fromhex(user_found.password), bytes.fromhex(user_found.salt), password):
            raise IncorrectPasswordError("The provided username and password don't match!")
        today = date.today()
        user_found.last_login = today.strftime("%m/%d/%y")
        self.blogger_repo.update(user_found)
        self.blogger_repo.save()
        return user_found

    def try_login_username(self, username, password):
        self.blogger_repo.load()  # not sure if we should refresh here, or in the find_by_uname() repo function
        user_found: Blogger = self.blogger_repo.find_by_username(username)
        if user_found is None:
            raise UsernameNotFoundError(f'No such username: {username} found!')
        if not self.hasher.check_pass(user_found.password, user_found.salt, password):
            raise IncorrectPasswordError("The provided username and password don't match!")
        today = date.today()
        user_found.last_login = today.strftime("%m/%d/%y")
        self.blogger_repo.update(user_found)
        self.blogger_repo.save()
        return user_found
