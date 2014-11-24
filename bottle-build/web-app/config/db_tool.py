from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables.base import *

class DBTool:
    user = 'webapp'
    password = 'webapp@www'
    host = 'localhost'
    dbname = 'Webapp'
    
    def get_engine(self):
        engine = create_engine('mysql+mysqldb://'+self.user+':'+ self.password + '@' + \
                                self.host+'/'+self.dbname)
        Base.metadata.create_all(engine)
        return engine

    def build_connection(self):
        Session = sessionmaker(bind=self.get_engine())
        self.session = Session()
        return self.session
