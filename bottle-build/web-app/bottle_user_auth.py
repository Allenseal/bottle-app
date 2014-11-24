# -*- coding: UTF-8 -*-
import inspect
from bottle import request, response
from tables.user import User

class AuthPlugin(object):

    name = 'user_auth'
    api = 2

    def __init__(self, keyword='user'):
        self.keyword = keyword

    def setup(self, app):
        ''' Make sure that other installed plugins don't affect the same
            keyword argument.'''
        for other in app.plugins:
            if not isinstance(other, AuthPlugin): continue
            if other.keyword == self.keyword:
                raise PluginError("Found another sqlite plugin with "\
                "conflicting settings (non-unique keyword).")

    def apply(self, callback, context):
        # Override global configuration with route-specific values.
        conf = context.config.get('user') or {}
        keyword = conf.get('keyword', self.keyword)

        # Test if the original callback accepts a 'user' keyword.
        args = inspect.getargspec(context.callback)[0]
        if keyword not in args:
            return callback

        def wrapper(*args, **kwargs):
            session = kwargs['db']

            auth_data = request.auth
            user = None
            if auth_data:
                account, secret = auth_data[0], auth_data[1]
                user = User.authenticate(session, account, secret)
                kwargs[keyword] = user
                if user:
                    rv = callback(*args, **kwargs)
                    return rv

            response.status = 401
            response.set_header('WWW-Authenticate', 'Basic realm="ssbox"')
            return { 'error': 'Authorization required' }

        # Replace the route callback with the wrapped one.
        return wrapper
