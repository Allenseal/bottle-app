from bottle import get, post, put, delete, run, request, default_app, response, HTTPError, install
from config.db_tool import DBTool
from bottle.ext.sqlalchemy import SQLAlchemyPlugin
from tables.applicant import Applicant
from bottle_user_auth import AuthPlugin
import base64

db_tool = DBTool()
install(SQLAlchemyPlugin(db_tool.get_engine()))
install(AuthPlugin())

@post('/api/post_db')
def post_db(db,user):
    name = request.forms.name
    email = request.forms.email
    new_applicant  = Applicant(account=name, email=email)
    db.add(new_applicant)
    db.commit()
    return {'status': 'sent'}

@get('/api/hello')
def get_hello(db, user):
    return {'content': 'hello'}

@post('/api/hello')
def post_hello(db, user):
    email = request.forms.email

    return {'content': 'hello', 'name': user.account, 'email': email}


application = default_app()
