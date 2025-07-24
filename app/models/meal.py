from app import db
from datetime import date

class Refeicao(db.Model):
    __tablename__ = 'refeicoes'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False, unique=True, default=date.today)
    quantidade_vagas = db.Column(db.Integer, nullable=False)

    # Relacionamento: uma refeição tem várias inscrições
    inscricoes = db.relationship('Inscricao', back_populates='refeicao', lazy='dynamic')

    def __repr__(self):
        return f"<Refeicao {self.data} - {self.quantidade_vagas} vagas>"
