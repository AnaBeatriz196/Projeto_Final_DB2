from flask import Flask

def create_app():
    app = Flask(__name__)

    # Aqui você pode registrar Blueprints, configurar o app, etc.
    return app
