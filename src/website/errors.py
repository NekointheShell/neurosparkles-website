class Error(Exception):
    def __init__(self):
        super().__init__()


class FailedLoginError(Exception):
    def __init__(self, attempted_user, remote_addr):
        super().__init__('Failed login for {} by {}'.format(attempted_user, remote_addr))
