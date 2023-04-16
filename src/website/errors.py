from flask import request


class Error(Exception):
    def __init__(self, message):
        super().__init__(message)


class FormNotValidError(Error):
    def __init__(self, username = None):
        if username == None: super().__init__('Form not valid by {}'.format(request.remote_addr))
        else: super().__init__('Form not valid by {}'.format(username))


class InvalidInputError(Error):
    def __init__(self, username = None):
        if username == None: super().__init__('Invalid input by {}'.format(request.remote_addr))
        else: super().__init__('Invalid input by {}'.format(username))


class InvalidEmailError(Error):
    def __init__(self, username = None):
        if username == None: super().__init__('Invalid email by {}'.format(request.remote_addr))
        else: super().__init__('Invalid email by {}'.format(username))


class DuplicateUserError(Error):
    def __init__(self, username = None):
        if username == None: super().__init__('Duplicate user by {}'.format(request.remote_addr))
        else: super().__init__('Duplicate user by {}'.format(username))


class FailedLoginError(Error):
    def __init__(self, username):
        super().__init__('Failed login for {} by {}'.format(username, request.remote_addr))


class NotLoggedInError(Error):
    def __init__(self):
        super().__init__('User is not logged in from {}'.format(request.remote_addr))


class AttemptedAdminAccessError(Error):
    def __init__(self, email):
        super().__init__('User {} attempted to access an admin page'.format(email))
