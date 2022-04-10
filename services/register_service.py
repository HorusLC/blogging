import re
from datetime import date

from Exceptions.usererror import UsernameExistsError, EmailExistsError
from dao.blogger_repository import BloggerRepository
from entity.blogger import Blogger
from services.phasher import PassHasher
from entity.user_enums import Role


class RegistrationService:
    def __init__(self, blogger_repo, hasher):
        self.blogger_repo: BloggerRepository = blogger_repo
        self.hasher: PassHasher = hasher

    def check_username(self, username):
        self.blogger_repo.load()
        u_found = self.blogger_repo.find_by_username(username)
        if u_found:
            raise UsernameExistsError(f'The username: {username} already exists! Did you forget your password?')
        return None

    def check_email(self, email):
        self.blogger_repo.load()
        u_found = self.blogger_repo.find_by_email(email)
        if u_found:
            raise EmailExistsError(f'The email: {email} already exists! Did you forget your password?')
        return None

    def validate_user_data(self, blogger):
        error_list = list()
        if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', blogger.password):
            error_list.append(
                'Password must be 8 chars long, must contain lower letter,upper letter, digit and special character')
        if not re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', blogger.email):
            error_list.append('Invalid email format!')
        if len(blogger.f_name) > 15 or len(blogger.f_name) < 2:
            error_list.append('Non valid first name!')
        if len(blogger.l_name) > 15 or len(blogger.l_name) < 2:
            error_list.append('Non valid last name!')
        return error_list

    def register(self, blogger):
        self.check_username(blogger.username)
        self.check_email(blogger.email)
        salt, pass_hash = self.hasher.hash_password(blogger.password)
        today = date.today()
        blogger.password = pass_hash.hex()
        blogger.salt = salt.hex()
        blogger.date_reg = today.strftime("%m/%d/%y")
        blogger.last_login = today.strftime("%m/%d/%y")
        blogger.blogs_followed = []
        blogger.role = Role.BLOGGER
        blogger = self.blogger_repo.create(blogger)
        self.blogger_repo.save()

    def register_fields(self, f_name, l_name, username, password, introduction, gender, email):

        self.check_username(username)
        self.check_email(email)
        secret = self.hasher.hash_password(password)
        today = date.today()
        reg_usr = Blogger(f_name, l_name, username, secret[0], secret[1], gender, email,
                          today.strftime("%m/%d/%y"), last_login=today.strftime("%m/%d/%y"),
                          introduction=introduction)
        reg_usr = self.blogger_repo.create(reg_usr)
        self.blogger_repo.save()
        return reg_usr
