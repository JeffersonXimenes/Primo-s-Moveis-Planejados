from infraestrutura.sql_alchemy import banco


class FeedbackModel(banco.Model):
    __tablename__ = 'tFeedback'

    cFeedback = banco.Column(banco.Integer, primary_key=True)
    ambiente = banco.Column(banco.String(255), nullable = False)
    notaAtendimento = banco.Column(banco.Integer, nullable=False)
    notaVendedor = banco.Column(banco.Integer, nullable=False)
    notaMontagem = banco.Column(banco.Integer, nullable=False)
    mensagem = banco.Column(banco.String(2555),nullable=True)
    cPedido = banco.Column(banco.Integer, banco.ForeignKey('tVendas.cPedido'), nullable=False)

    def __init__(self, cFeedback, ambiente, notaAtendimento, notaVendedor, notaMontagem,mensagem,cPedido):
        self.cFeedback = cFeedback
        self.ambiente = ambiente
        self.notaAtendimento = notaAtendimento
        self.notaVendedor = notaVendedor
        self.notaMontagem = notaMontagem
        self.mensagem = mensagem
        self.cPedido = cPedido

    def json(self):
        return {
            'cFeedback': self.cFeedback,
            'ambiente': self.ambiente,
            'notaAtendimento': self.notaAtendimento,
            'notaVendedor': self.notaVendedor,
            'notaMontagem': self.notaMontagem,
            'mensagem': self.mensagem,
            'cPedido': self.cPedido
        }

    @classmethod
    def find_feed(cls, cFeedback):
        feed = cls.query.filter_by(cFeedback=cFeedback).first()
        if feed:
            return feed
        return None

    def save_feed(self):
        banco.session.add(self)
        banco.session.commit()

    def update_feed(self, ambiente, notaAtendimento, notaVendedor, notaMontagem,mensagem,cPedido):
        self.ambiente = ambiente
        self.notaAtendimento = notaAtendimento
        self.notaVendedor = notaVendedor
        self.notaMontagem = notaMontagem
        self.mensagem = mensagem
        self.cPedido = cPedido

    def delete_feed(self):
        banco.session.delete(self)
        banco.session.commit()
