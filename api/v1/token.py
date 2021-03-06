from flask import current_app, jsonify

from api.libs.enums import ClientTypeEnum
from api.libs.redprint import Redprint
from models.user import User
from validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
api = Redprint('token')


@api.route('/',methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    identity = promise[form.type.data](form.account.data, form.secret.data)
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'], expiration)

    t = {
        'token' : token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, exporation=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=exporation)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })
