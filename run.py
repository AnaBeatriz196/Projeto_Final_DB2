from app import create_app, db
from flask_migrate import Migrate
from app.routes.admin import admin_bp
from app.routes.auth import auth_bp
from app.routes.report import report_bp
from app.routes.student import student_bp
from flask import Flask



def create_app():
    app = Flask(__name__)

    # Registra o blueprint
    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(student_bp)

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

