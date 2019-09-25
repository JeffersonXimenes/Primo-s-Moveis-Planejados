from sql_alchemy import banco

class ClienteModel(banco.Model):
    __tablename__ = 'clientes'

    cCliente = banco.Column(banco.String, primary_key=True)
    nCpf = banco.Column(banco.String(20), primary_key=True)
    nome = banco.Column(banco.String(80))
    dataNascimento = banco.Column(banco.String(20))
    dataCadastro = banco.Column(banco.String(20))

    def __init__(self, cCliente, nCpf, nome, dataNascimento, dataCadastro):
        self.cCliente = cCliente
        self.nCpf = nCpf
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.dataCadastro = dataCadastro

    def json(self):
        return {
            'cCliente': self.cCliente,
            'nCpf': self.nCpf,
            'nome': self.nome,
            'dataNascimento': self.dataNascimento,
            'dataCadastro': self.dataCadastro
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

    def update_cliente(self, nCpf, nome, dataNascimento, dataCadastro):
        self.nCpf = nCpf
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.dataCadastro = dataCadastro

    def delete_cliente(self):
        banco.session.delete(self)
        banco.session.commit()
