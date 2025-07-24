from app import create_app, db
from flask_migrate import Migrate

app = create_app()

# Para permitir que o Flask CLI encontre `db`
from app.models import user, meal, form  # ou inscrição

if __name__ == '__main__':
    app.run(debug=True)
