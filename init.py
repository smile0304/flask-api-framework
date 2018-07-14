from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from api.libs.error_code import ServerError

class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
