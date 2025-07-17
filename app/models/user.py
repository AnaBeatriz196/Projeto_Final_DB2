from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # 'aluno', 'admin', 'intermediario'
    ativo = db.Column(db.Boolean, default=True)

    # Relacionamentos (se quiser associar com inscrições, por exemplo)
    inscricoes = db.relationship('Inscricao', back_populates='aluno', lazy='dynamic')

    def set_password(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return f'<User {self.nome} ({self.tipo})>'
