from app import db
from datetime import datetime

class Inscricao(db.Model):
    __tablename__ = 'inscricoes'

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    refeicao_id = db.Column(db.Integer, db.ForeignKey('refeicoes.id'), nullable=False)
    horario_inscricao = db.Column(db.DateTime, default=datetime.utcnow)
    compareceu = db.Column(db.Boolean, default=None)  # True, False ou None (não avaliado ainda)

    # Relacionamentos
    aluno = db.relationship('User', back_populates='inscricoes')
    refeicao = db.relationship('Refeicao', back_populates='inscricoes')

    @property
    def data(self):
        return self.refeicao.data if self.refeicao else None

    def __repr__(self):
        return f'<Inscricao aluno={self.aluno_id} data={self.data}>'
