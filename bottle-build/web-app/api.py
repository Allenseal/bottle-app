from bottle import get, post, request, default_app, response, HTTPError
from config.db_tool import DBTool
from tables.applicant import Applicant

#TODO please create db first
'''
db_tool = DBTool()
session = db_tool.build_connection()
@post('/api/post_db')
def post_db():
    name = request.forms.name
    email = request.forms.email
    new_applicant  = Applicant(name=name, email=email)
    session.add(new_applicant)
    session.commit()
    return {'status': 'sent'}

'''

@get('/api/hello')
def get_hello():
    return {'content': 'hello'}

@post('/api/hello')
def post_hello():
    name = request.forms.name
    email = request.forms.email

    return {'content': 'hello', 'name': name, 'email': email}



application = default_app()
