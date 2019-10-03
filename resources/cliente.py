from flask_restful import Resource, reqparse
from flask import jsonify, request
from models.clientes import ClienteModel
from infraestrutura.validacoes import validar_data
from infraestrutura.to_dict import to_dict, to_dict_list

class CpfInvalido(Exception):
    pass
class ClienteNaoEncontrado(Exception):
    pass
class ClienteJaCadastrado(Exception):
    pass
class DataInvalida(Exception):
    pass
class CpfJaCadastrado(Exception):
    pass

class Clientes(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cCliente', type=int)
    atributos.add_argument('nCpf', type=int)
    atributos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank.")
    atributos.add_argument('dataNascimento', type=str)
    atributos.add_argument('dataCadastro', type=str)
    def get(self):
        return {'clientes': [cliente.json() for cliente in ClienteModel.query.all()]} # SELECT * FROM clientes
    def post(self):
        dados = Clientes.atributos.parse_args()
        id = dados['cCliente']
        dataNascimento = dados['dataNascimento']
        dataCadastro = dados['dataCadastro']
        cpf = dados['nCpf']
        if len(str(cpf)) != 11:
            raise CpfInvalido()
            #return {"mensagem": "CPF invalido."}, 500
        if ClienteModel.find_cliente(id):
            raise ClienteJaCadastrado()
            #return {"menssagem": "Cliente id '{}' já existe.".format(id)}, 400 #Bad Request
        if validar_data(dataNascimento) and validar_data(dataCadastro):
            cliente = ClienteModel(**dados)

            try:
                cliente.save_cliente()
            except:
                raise CpfJaCadastrado()
                #return {"mensagem": "Ocorreu um erro ao inserir o cliente, verique a integridade."}, 500 #Internal Server Error
            return cliente.json()
        else:
             raise DataInvalida()

class Cliente(Resource):

    atributos = reqparse.RequestParser()
    atributos.add_argument('nCpf', type=int)
    atributos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank.")
    atributos.add_argument('dataNascimento',type=str)
    atributos.add_argument('dataCadastro' , type=str)

    def get(self, cCliente):
        cliente = ClienteModel.find_cliente(cCliente)
        if cliente:
            return cliente.json()
        raise ClienteNaoEncontrado()

    def put(self, cCliente):
        dados = Cliente.atributos.parse_args()
        dataNascimento = dados['dataNascimento']
        dataCadastro = dados['dataCadastro']
        cpf = dados['nCpf']
        if len(str(cpf)) != 11:
            raise CpfInvalido()
            #return {"mensagem": "CPF invalido."}, 500
        if validar_data(dataNascimento) and validar_data(dataCadastro):
            cliente = ClienteModel(cCliente, **dados)
            cliente_encontrado = ClienteModel.find_cliente(cCliente)
            if cliente_encontrado == None:
                raise ClienteNaoEncontrado()
            try:
                if cliente_encontrado:
                    cliente_encontrado.update_cliente(**dados)
                    cliente_encontrado.save_cliente()
                    return cliente_encontrado.json()

                    cliente.save_cliente()

            except:
                raise CpfJaCadastrado()
                #return {"mensagem": "Ocorreu um erro ao inserir o cliente. Verique a integridade"}, 500 #Internal Server Error
            return cliente.json()
        else:
            raise DataInvalida()
            #return {"mensagem": "Data invalida."}, 500
'''
    def delete(self, cCliente):
        cliente = ClienteModel.find_cliente(cCliente)
        if cliente:
            cliente.delete_cliente()
            return {'messagem': 'Cliente deletado.'}
        return {'menssagem': 'Cliente não encontrado.'}, 404
'''