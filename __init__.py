from init import Flask


def register_blueprints(app):
    from api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(),url_prefix='/v1')

def register_plugin(app):
    from models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def creat_app():

    app = Flask(__name__)
    app.config.from_object('config.settings')
    app.config.from_object('config.secure')
    register_blueprints(app)
    register_plugin(app)
    return app