from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables.base import *

class DBTool:
    user = 'test'
    password = 'test'
    host = 'localhost'
    dbname = 'test_db'
    def get_engine(self):
        engine = create_engine('mysql+mysqldb://'+self.user+':'+ self.password + '@' + \
                                self.host+'/'+self.dbname)
        Base.metadata.create_all(engine)
        return engine

    def build_connection(self):
        Session = sessionmaker(bind=self.get_engine())
        self.session = Session()
        return self.session
