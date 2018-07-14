from http.client import HTTPException
from flask import Flask

from api.libs.error import APIException
from api.libs.error_code import ServerError
from . import creat_app

app = creat_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e,APIException):
        return e
    if isinstance(e,HTTPException):
        code = e.code
        msg = e.description
        error_code =1007
        return APIException(msg,code,error_code)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e
    return APIException()


if __name__ == '__main__':
    app.run()

