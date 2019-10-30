from infraestrutura.sql_alchemy import banco 


class TipoPagamentoModel(banco.Model):
    __tablename__ = 'tTipoPagamento'
    
    cTipoPagamento = banco.Column(banco.Integer, primary_key=True)
    nParcelas = banco.Column(banco.Integer, nullable = True)
    Formapagamento = banco.Column(banco.String(255), nullable = True)



    def __init__(self, cTipoPagamento, nParcelas,Formapagamento):
        self.cTipoPagamento = cTipoPagamento
        self.nParcelas = nParcelas
        self.Formapagamento = Formapagamento


    def json(self):
        return {
            'cTipoPagamento': self.cTipoPagamento,
            'nParcelas': self.nParcelas,
            'Formapagamento': self.Formapagamento,

        }

    @classmethod
    def find_TipoPagamento(cls, cTipoPagamento):
        pagamento = cls.query.filter_by(cTipoPagamento=cTipoPagamento).first()
        if pagamento:
            return pagamento
        return None

    def save_TipoPagamento(self):
        banco.session.add(self)
        banco.session.commit()

    def update_TipoPagamento(self, nParcelas,Formapagamento):
        self.nParcelas = nParcelas
        self.Formapagamento = Formapagamento


