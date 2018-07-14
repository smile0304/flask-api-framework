from flask import jsonify, g, Response

from api.libs.error_code import DeleteSuccess, AuthFailed
from api.libs.redprint import Redprint
from api.libs.token_auth import auth
from models.base import db
from models.user import User

api = Redprint('user')


@api.route('/<int:uid>/', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.id
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/<int:uid>/', methods=['DELETE'])
def super_delete_user(uid):
    return Response()


@api.route('/', methods=['DELETE'])
@auth.login_required
def delect_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id = uid).first_or_404()
        user.delete()
    return DeleteSuccess()