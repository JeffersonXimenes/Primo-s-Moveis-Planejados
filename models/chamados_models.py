from infraestrutura.sql_alchemy import banco


class ChamadoModel(banco.Model):
    __tablename__ = 'tChamados'

    cChamado = banco.Column(banco.Integer, primary_key=True)
    cPedido = banco.Column(banco.Integer, banco.ForeignKey('tVendas.cPedido'), nullable=False)
    movel = banco.Column(banco.String(255), nullable=False)
    tipoOcorrencia = banco.Column(banco.String(255), nullable=False)
    descricao = banco.Column(banco.String(255), nullable=False)
    dataAgendada = banco.Column(banco.String(10), nullable=False)
    


    def __init__(self, cChamado, cPedido, movel, tipoOcorrencia, descricao,dataAgendada):
        self.cChamado = cChamado
        self.cPedido = cPedido
        self.movel = movel
        self.tipoOcorrencia = tipoOcorrencia
        self.descricao = descricao
        self.dataAgendada = dataAgendada


    def json(self):
        return {
            'cChamado': self.cChamado,
            'cPedido': self.cPedido,
            'movel': self.movel,
            'tipoOcorrencia': self.tipoOcorrencia,
            'descricao': self.descricao,
            'dataAgendada': self.dataAgendada,

        }

    @classmethod
    def find_chamado(cls, cChamado):
        chamado = cls.query.filter_by(cChamado=cChamado).first()
        if chamado:
            return chamado
        return None

    def save_chamado(self):
        banco.session.add(self)
        banco.session.commit()

    def update_chamado(self, cPedido, movel, tipoOcorrencia, descricao,dataAgendada):
        self.cPedido = cPedido
        self.movel = movel
        self.tipoOcorrencia = tipoOcorrencia
        self.descricao = descricao
        self.dataAgendada = dataAgendada


    def delete_chamado(self):
        banco.session.delete(self)
        banco.session.commit()
