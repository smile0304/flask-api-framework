
class BaseScope:
    allow_api = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        #支持链式操作
        self.allow_api = list(set(self.allow_api))
        return self


class AdminScope:
    allow_api = ['v1.super_get_user']


class UserScope:
    allow_api = []


class SuperScope:
    allow_api = ['v1.C', 'v1.D']

    def __init__(self):
        self.add(UserScope())

    def add(self,other):
        self.allow_api = self.allow_api + other.allow_api
        #支持链式操作
        return self


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    read_name = splits[0]
    if endpoint in scope.allow_api:
        return True
    if read_name in scope.allow_moudle:
        return True
    else:
        return False