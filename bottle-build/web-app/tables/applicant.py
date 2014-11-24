from base import *


class Applicant(Base):
    __tablename__ = 'applicants'

    id = Column(Integer, primary_key = True)
    account = Column(String(100))
    email = Column(String(100))
