from infraestrutura.sql_alchemy import banco

class AcompanhamentoPedidoModel(banco.Model):
    __tablename__ = 'tAcompanhamentoPedido'

    cAcompanhamento = banco.Column(banco.Integer, primary_key=True)
    iDescricao = banco.Column(banco.String(500), nullable=False) 
    dataAtualizacao = banco.Column(banco.String(20), nullable=False)
    cFuncionario = banco.Column(banco.Integer, banco.ForeignKey('tFuncionarios.cFuncionario'), nullable=False)
    cPedido = banco.Column(banco.Integer, banco.ForeignKey('tVendas.cPedido'), nullable=False)

    def __init__(self, cAcompanhamento, iDescricao, dataAtualizacao, cFuncionario, cPedido):
        self.cAcompanhamento = cAcompanhamento
        self.iDescricao = iDescricao
        self.dataAtualizacao = dataAtualizacao
        self.cFuncionario = cFuncionario
        self.cPedido = cPedido

    def json(self):
        return {
            'cAcompanhamento': self.cAcompanhamento,
            'iDescricao': self.iDescricao,
            'dataAtualizacao': self.dataAtualizacao,
            'cFuncionario': self.cFuncionario,
            'cPedido': self.cPedido
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

