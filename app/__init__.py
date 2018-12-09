from flask import Flask


def create_app():
    application = Flask(__name__, static_url_path='/static')
    application.config.update(SECRET_KEY='SECRET-KEY')
    from app.main import bp as main_bp
    application.register_blueprint(main_bp)

    return application
