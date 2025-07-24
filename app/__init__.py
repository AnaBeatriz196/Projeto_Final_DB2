from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    load_dotenv()  # Carrega variáveis do .env

    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Importar modelos aqui para o Migrate reconhecê-los
    from app.models import user, meal, form  # ou inscrição, dependendo do nome do arquivo

    # Registrar blueprints
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.student import student_bp
    from app.routes.report import report_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(report_bp)

    return app
