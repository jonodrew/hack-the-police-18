from flask import Flask
import os


def create_app():
    application = Flask(__name__, static_url_path='/static')

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static', 'customlogos')
    application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    application.config.update(SECRET_KEY='SECRET-KEY')

    from app.main import bp as main_bp
    application.register_blueprint(main_bp)

    return application
