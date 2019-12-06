from infraestrutura.sql_alchemy import banco
from infraestrutura.validacoes import getData

class AcompanhamentoPedidoModel(banco.Model):
    __tablename__ = 'tAcompanhamentoPedido'

    cAcompanhamento = banco.Column(banco.Integer, primary_key=True)
    cFuncionario = banco.Column(banco.Integer, banco.ForeignKey('tFuncionarios.cFuncionario'), nullable=False)
    cPedido = banco.Column(banco.Integer, banco.ForeignKey('tVendas.cPedido'), nullable=False)
    iDescricao = banco.Column(banco.String(500), nullable=False) 
    dataAtualizacao = banco.Column(banco.String(20), nullable=False)

    def __init__(self, cAcompanhamento, cFuncionario, cPedido, iDescricao):
        self.cAcompanhamento = cAcompanhamento
        self.cFuncionario = cFuncionario
        self.cPedido = cPedido
        self.iDescricao = iDescricao
        self.dataAtualizacao = getData()

    def json(self):
        return {
            'cAcompanhamento': self.cAcompanhamento,
            'cFuncionario': self.cFuncionario,
            'cPedido': self.cPedido,
            'iDescricao': self.iDescricao,
            'dataAtualizacao': self.dataAtualizacao,
        }
    
    @classmethod
    def find_acompanhamento(cls, cAcompanhamento):
        acompanhamento = cls.query.filter_by(cAcompanhamento=cAcompanhamento).first()
        if acompanhamento:
            return acompanhamento
        return None

    def save_acompanhamento(self):
        banco.session.add(self)
        banco.session.commit()

