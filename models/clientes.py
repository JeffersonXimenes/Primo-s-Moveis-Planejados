from infraestrutura.sql_alchemy import banco

class ClienteModel(banco.Model):
    __tablename__ = 'tClientePF'

    cCliente = banco.Column(banco.Integer, primary_key = True,  nullable = False)
    nCpf = banco.Column(banco.String(11), unique = True, nullable = False)
    iNome = banco.Column(banco.String(255),nullable = False)
    iEmail = banco.Column(banco.String(255), nullable=False)
    dataNascimento = banco.Column(banco.String(20),nullable=False)
    dataCadastro = banco.Column(banco.String(20),nullable=False)
    iProcedencia = banco.Column(banco.String(255))

    def __init__(self,cCliente, nCpf, iNome, iEmail, dataNascimento, dataCadastro,iProcedencia):
        self.cCliente = cCliente
        self.nCpf = nCpf
        self.iNome = iNome
        self.iEmail = iEmail
        self.dataNascimento = dataNascimento
        self.dataCadastro = dataCadastro
        self.iProcedencia = iProcedencia

    def json(self):
        return {
            'cCliente': self.cCliente,
            'nCpf': self.nCpf,
            'iNome': self.iNome,
            'iEmail': self.iEmail,
            'dataNascimento': self.dataNascimento,
            'dataCadastro': self.dataCadastro,
            'iProcedencia': self.iProcedencia
        }

    @classmethod
    def find_cliente(cls, cCliente):
        cliente = cls.query.filter_by(cCliente=cCliente).first()
        if cliente:
            return cliente
        return None

    def save_cliente(self):
        banco.session.add(self)
        banco.session.commit()

    def update_cliente(self, nCpf, iNome, iEmail, dataNascimento, dataCadastro,iProcedencia):
        self.nCpf = nCpf
        self.iNome = iNome,
        self.iEmail = iEmail,
        self.dataNascimento = dataNascimento
        self.dataCadastro = dataCadastro,
        self.iProcedencia = iProcedencia

    def delete_cliente(self):
        banco.session.delete(self)
        banco.session.commit()
