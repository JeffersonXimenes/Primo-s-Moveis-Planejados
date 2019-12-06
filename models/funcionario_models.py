from infraestrutura.sql_alchemy import banco


class FuncionarioModel(banco.Model):
    __tablename__ = 'tFuncionarios'

    cFuncionario = banco.Column(banco.Integer, primary_key=True)
    iNome = banco.Column(banco.String(255), nullable = False)
    nMatricula = banco.Column(banco.String(20) , unique=True, nullable = False)
    dataNascimento = banco.Column(banco.String(20), nullable = False)
    nCpf = banco.Column(banco.String(11), unique=True, nullable=False)
    cCargo = banco.Column(banco.Integer, banco.ForeignKey('tCargos.cCargos'), nullable=False)


    def __init__(self, cFuncionario, iNome, nMatricula, dataNascimento,nCpf, cCargo):
        self.cFuncionario = cFuncionario
        self.iNome = iNome
        self.nMatricula = nMatricula
        self.dataNascimento = dataNascimento
        self.nCpf = nCpf
        self.cCargo = cCargo

    def json(self):
        return {
            'cFuncionario': self.cFuncionario,
            'iNome': self.iNome,
            'nMatricula': self.nMatricula,
            'dataNascimento': self.dataNascimento,
            'nCpf': self.nCpf,
            'cCargo':self.cCargo
        }

    @classmethod
    def find_funcionario(cls, cFuncionario):
        funcionario = cls.query.filter_by(cFuncionario=cFuncionario).first()
        if funcionario:
            return funcionario
        return None
    @classmethod
    def find_ID_Matricula(cls, nMatricula):
        matricula = cls.query.filter_by(nMatricula=nMatricula).first()
        if matricula:
            return matricula.cFuncionario
        return None

    def save_funcionario(self):
        banco.session.add(self)
        banco.session.commit()

    def update_funcionario(self,iNome, nMatricula, dataNascimento,nCpf, cCargo):
        self.iNome = iNome
        self.nMatricula = nMatricula
        self.dataNascimento = dataNascimento
        self.nCpf = nCpf
        self.cCargo = cCargo

    def delete_funcionario(self):
        banco.session.delete(self)
        banco.session.commit()
