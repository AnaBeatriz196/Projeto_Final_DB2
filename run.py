from app import create_app, db
from flask_migrate import Migrate
from app.routes.admin import admin_bp
from app.routes.auth import auth_bp
from app.routes.report import report_bp
from app.routes.student import student_bp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()



def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'sua_chave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'  # ou seu banco

    db.init_app(app)
    login_manager.init_app(app)

    from app.models.user import User  # certifique-se de importar o User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



    login_manager.login_view = 'auth.login'  # redireciona para login se não autenticado
    login_manager.login_message_category = 'info'  # categoria do flash message

    # Registra o blueprint
    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(student_bp)


    return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)