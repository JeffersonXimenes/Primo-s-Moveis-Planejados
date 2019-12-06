from flask_restful import Resource, reqparse
from models.funcionario_models import FuncionarioModel
from infraestrutura.validacoes import validar_data
from models.cargo_models import CargoModel

class IdJaExiste (Exception):
    pass
class DataInvalida (Exception):
    pass
class CargoNaoExiste (Exception):
    pass
class CpfInvalido (Exception):
    pass
class ErroInserir (Exception):
    pass
class FuncionarioNaoExiste (Exception):
    pass

class Funcionarios(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cFuncionario', type=int)
    atributos.add_argument('iNome', type=str)
    atributos.add_argument('nMatricula', type=str)
    atributos.add_argument('dataNascimento', type=str)
    atributos.add_argument('nCpf', type=str)
    atributos.add_argument('cCargo', type=int)

    def get(self):
        return {'funcionarios': [funcionario.json() for funcionario in FuncionarioModel.query.all()]} # SELECT * FROM clientes
    def post(self, dados):
        dados = Funcionarios.atributos.parse_args()
        id = dados['cFuncionario']
        dataNascimento = dados['dataNascimento']
        id_cargo = dados['cCargo']
        cpf = dados['nCpf']
        if FuncionarioModel.find_funcionario(id):
            raise IdJaExiste()
        if not validar_data(dataNascimento):
            raise DataInvalida()
        if not CargoModel.find_cargo(id_cargo):
            raise CargoNaoExiste()
        if len(str(cpf)) != 11:
            raise CpfInvalido()
        funcionario = FuncionarioModel(**dados)
        try:
            funcionario.save_funcionario()
        except:
            raise ErroInserir()
        return funcionario.json()


class Funcionario(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('iNome', type=str)
    atributos.add_argument('nMatricula', type=str)
    atributos.add_argument('dataNascimento', type=str)
    atributos.add_argument('nCpf', type=str)
    atributos.add_argument('cCargo', type=int)

    def get(self, cFuncionario):
        funcionario = FuncionarioModel.find_funcionario(cFuncionario)
        if funcionario:
            return funcionario.json()
        raise FuncionarioNaoExiste()

    def put(self, cFuncionario):
        dados = Funcionario.atributos.parse_args()
        dataNascimento = dados['dataNascimento']
        id_cargo = dados['cCargo']
        cpf = dados['nCpf']
        if not CargoModel.find_cargo(id_cargo):
            raise CargoNaoExiste()
        if len(str(cpf)) != 11:
            raise CpfInvalido()
        if validar_data(dataNascimento) :
            funcionario = FuncionarioModel(cFuncionario, **dados)
            funcionario_encontrado = FuncionarioModel.find_funcionario(cFuncionario)
            try:
                if funcionario_encontrado:
                    funcionario_encontrado.update_funcionario(**dados)
                    funcionario_encontrado.save_funcionario()
                    return funcionario_encontrado.json()

                funcionario.save_funcionario()
            except:
                raise ErroInserir()
            return funcionario.json()
        else:
            raise DataInvalida()

    def delete(self, cFuncionario):
        funcionario = FuncionarioModel.find_funcionario(cFuncionario)
        if funcionario:
            funcionario.delete_funcionario()
            return {'messagem': 'funcionario deletado.'}
        raise FuncionarioNaoExiste()

