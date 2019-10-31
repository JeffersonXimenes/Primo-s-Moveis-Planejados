from infraestrutura.sql_alchemy import banco


class VendasModel(banco.Model):
    __tablename__ = 'tVendas'

    cPedido = banco.Column(banco.Integer, primary_key=True)
    cCliente = banco.Column(banco.Integer, banco.ForeignKey('tClientePF.cCliente'), nullable = False)
    cFuncionario = banco.Column(banco.Integer, banco.ForeignKey('tFuncionarios.cFuncionario'), nullable=False)
    dataVenda = banco.Column(banco.String(20), nullable=False)
    nContrato = banco.Column(banco.String(20), nullable = False)
    iTipoContrato = banco.Column(banco.String(255), nullable=False)
    cTipoPagamento = banco.Column(banco.Integer, banco.ForeignKey('tTipoPagamento.cTipoPagamento'), nullable=False)


    def __init__(self, cPedido, cCliente, cFuncionario, dataVenda, nContrato,iTipoContrato,cTipoPagamento):
        self.cPedido = cPedido
        self.cCliente = cCliente
        self.cFuncionario = cFuncionario
        self.dataVenda = dataVenda
        self.nContrato = nContrato
        self.iTipoContrato = iTipoContrato
        self.cTipoPagamento = cTipoPagamento

    def json(self):
        return {
            'cPedido': self.cPedido,
            'cCliente': self.cCliente,
            'cFuncionario': self.cFuncionario,
            'dataVenda': self.dataVenda,
            'nContrato': self.nContrato,
            'iTipoContrato': self.iTipoContrato,
            'cTipoPagamento': self.cTipoPagamento
        }

    @classmethod
    def find_venda(cls, cPedido):
        venda = cls.query.filter_by(cPedido=cPedido).first()
        if venda:
            return venda
        return None

    def save_venda(self):
        banco.session.add(self)
        banco.session.commit()

    def update_venda(self, cCliente, cFuncionario, dataVenda, nContrato,iTipoContrato,cTipoPagamento):
        self.cCliente = cCliente
        self.cFuncionario = cFuncionario
        self.dataVenda = dataVenda
        self.nContrato = nContrato
        self.iTipoContrato = iTipoContrato
        self.cTipoPagamento = cTipoPagamento

    def delete_venda(self):
        banco.session.delete(self)
        banco.session.commit()
