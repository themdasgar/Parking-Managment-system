from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app






class Config:
    
    SECRET_KEY = 'mera-secret-key-Asgar@802219'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:TUMHARA_PASSWORD@localhost/parking_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
