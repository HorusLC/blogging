import hmac
import os
from hashlib import pbkdf2_hmac


class PassHasher:
    method: str = 'sha256'
    iterations: int = 300000
    salt_size: int = 16

    def __init__(self):
        pass

    @classmethod
    def hash_password(cls, password: str):
        salt = os.urandom(cls.salt_size)
        p_hash = pbkdf2_hmac(cls.method, password.encode(), salt, cls.iterations)
        return salt, p_hash

    @classmethod
    def check_pass(cls, pass_hash: bytes, pass_salt: bytes, password: str):
        check_hash = pbkdf2_hmac(cls.method, password.encode(), pass_salt, cls.iterations)
        return hmac.compare_digest(pass_hash, check_hash)

