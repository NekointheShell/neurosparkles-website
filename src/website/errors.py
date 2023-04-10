from flask import request


class Error(Exception):
    def __init__(self):
        super().__init__()


class FailedLoginError(Exception):
    def __init__(self, attempted_user):
        super().__init__('Failed login for {} by {}'.format(attempted_user, request.remote_addr))


class InvalidEmailError(Exception):
    def __init__(self, email):
        super().__init__('Invalid email {} by {}'.format(email, request.remote_addr))


class RoleError(Exception):
    def __init__(self, email, role):
        super().__init__('Invalid role {} for {}'.format(role, email))
