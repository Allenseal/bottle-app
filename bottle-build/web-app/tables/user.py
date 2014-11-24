from base import *
import hashlib
import os
import pwd
import grp
import requests

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    account = Column(String)
    passwd = Column(String(32))
    is_admin = Column(Boolean)
    is_suspended = Column(Boolean)
    is_deleted = Column(Boolean)

    @classmethod
    def authenticate(cls, session, account, secret):
        user = session.query(User).filter(User.account==account).first()
        valid = False
        if user:
            valid = user.validate_password(secret) and user.is_valid()
        if valid:
            return user
        else:
            return None

    def validate_password(self, password):
        pwd_hash = hashlib.md5(password).hexdigest()
        #TO-DO remove md5 check
        return (pwd_hash == self.passwd or password == self.passwd)

    def is_valid(self):
        return not (self.is_deleted or self.is_suspended)
