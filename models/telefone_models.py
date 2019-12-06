from infraestrutura.sql_alchemy import banco
from infraestrutura.validacoes import getData


class TelefoneModel(banco.Model):
    __tablename__ = 'telefones'

    cTelefone = banco.Column(banco.Integer, primary_key=True)
    cCliente = banco.Column(banco.Integer, banco.ForeignKey('tClientePF.cCliente'), nullable = False)
    cDDD = banco.Column(banco.Integer, nullable = False)
    nTelefone = banco.Column(banco.Integer , nullable = False)
    dataAtualizacao = banco.Column(banco.String(20), nullable = False)


    def __init__(self, cTelefone, cCliente, cDDD, nTelefone):
        self.cTelefone = cTelefone
        self.cCliente = cCliente
        self.cDDD = cDDD
        self.nTelefone = nTelefone
        self.dataAtualizacao = getData()

    def json(self):
        return {
            'cTelefone': self.cTelefone,
            'cCliente': self.cCliente,
            'cDDD': self.cDDD,
            'nTelefone': self.nTelefone,
            'dataAtualizacao': self.dataAtualizacao
        }

    @classmethod
    def find_telefone(cls, cTelefone):
        telefone = cls.query.filter_by(cTelefone=cTelefone).first()
        if telefone:
            return telefone
        return None

    def save_telefone(self):
        banco.session.add(self)
        banco.session.commit()

    def update_telefone(self, cCliente, cDDD, nTelefone, dataAtualizacao):
        self.cCliente = cCliente
        self.cDDD = cDDD
        self.nTelefone = nTelefone
        self.dataAtualizacao = dataAtualizacao

    def delete_telefone(self):
        banco.session.delete(self)
        banco.session.commit()
