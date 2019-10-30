from infraestrutura.sql_alchemy import banco


class EnderecoModel(banco.Model):
    __tablename__ = 'tEnderecos'

    cEndereco = banco.Column(banco.Integer, primary_key=True)
    cCliente = banco.Column(banco.Integer, banco.ForeignKey('tClientePF.cCliente'), nullable = False)
    nCep = banco.Column(banco.String(8), nullable=False)
    iEndereco = banco.Column(banco.String(255), nullable = False)
    numero = banco.Column(banco.String(6),nullable = False)
    iComplemento = banco.Column(banco.String(255),nullable = False)
    iBairro = banco.Column(banco.String(255), nullable = False)
    cUf = banco.Column(banco.String(2),nullable=False)
    dataAtualizacao = banco.Column(banco.String(20),nullable = False)




    def __init__(self, cEndereco, cCliente, nCep, iEndereco, numero ,iComplemento,iBairro,cUf,dataAtualizacao):
        self.cEndereco = cEndereco
        self.cCliente = cCliente
        self.nCep = nCep
        self.iEndereco = iEndereco
        self.numero = numero
        self.iComplemento = iComplemento
        self.iBairro = iBairro
        self.cUf = cUf
        self.dataAtualizacao = dataAtualizacao

    def json(self):
        return {
            'cEndereco': self.cEndereco,
            'cCliente': self.cCliente,
            'nCep': self.nCep,
            'iEndereco': self.iEndereco,
            'numero': self.numero,
            'iComplemento': self.iComplemento,
            'iBairro': self.iBairro,
            'cUf': self.cUf,
            'dataAtualizacao': self.dataAtualizacao
        }

    @classmethod
    def find_endereco(cls, cEndereco):
        endereco = cls.query.filter_by(cEndereco=cEndereco).first()
        if endereco:
            return endereco
        return None

    def save_endereco(self):
        banco.session.add(self)
        banco.session.commit()

    def update_endereco(self, cCliente, nCep, iEndereco,numero, iComplemento,iBairro,cUf,dataAtualizacao):
        self.cCliente = cCliente
        self.nCep = nCep
        self.iEndereco = iEndereco
        self.numero = numero
        self.iComplemento = iComplemento
        self.iBairro = iBairro
        self.cUf = cUf
        self.dataAtualizacao = dataAtualizacao

    def delete_endereco(self):
        banco.session.delete(self)
        banco.session.commit()
