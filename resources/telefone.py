from flask_restful import Resource, reqparse
from models.telefone_models import TelefoneModel
from infraestrutura.validacoes import validar_data
from models.clientes import ClienteModel


class TelefoneNaoExiste(Exception):
    pass
class DDDInvalido(Exception):
    pass
class NumeroInvalido(Exception):
    pass
class IdJaExiste(Exception):
    pass
class IdClienteNaoExiste(Exception):
    pass
class ErroInserir(Exception):
    pass
class DataInvalida(Exception):
    pass

class Telefones(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cTelefone', type=int)
    atributos.add_argument('cCliente', type=int)
    atributos.add_argument('cDDD', type=int)
    atributos.add_argument('nTelefone', type=int)
    atributos.add_argument('dataAtualizacao', type=str)

    def get(self):
        return {'telefones': [telefone.json() for telefone in TelefoneModel.query.all()]} # SELECT * FROM clientes
    def post(self):
        dados = Telefones.atributos.parse_args()
        id = dados['cTelefone']
        dataAtualizacao = dados['dataAtualizacao']
        id_cliente = dados['cCliente']
        numerotel = dados['nTelefone']
        ddd = dados['cDDD']
        if len(str(ddd)) != 2:
            raise DDDInvalido()
            #return {"mensagem": "DDD do telefone invalido"}
        if len(str(numerotel)) != 9:
            raise NumeroInvalido()
            #return {"mensagem": "Numero de telefone invalido"}, 500
        if TelefoneModel.find_telefone(id):
            raise IdJaExiste()
            #return {"menssagem": "Telefone id '{}' já existe.".format(id)}, 400 #Bad Request
        if not ClienteModel.find_cliente(id_cliente):
            raise IdClienteNaoExiste()
            #return {"mensagem": "ID do Cliente não existe."}, 500
        if validar_data(dataAtualizacao):
            telefone = TelefoneModel(**dados)
            try:
                telefone.save_telefone()
            except:
                raise ErroInserir()
                #return {"mensagem": "Ocorreu um erro ao inserir o telefone."}, 500 #Internal Server Error
            return telefone.json()
        else:
            raise DataInvalida()
             #return {"mensagem": "Data invalida."}, 500

class Telefone(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cCliente', type=int)
    atributos.add_argument('cDDD', type=int)
    atributos.add_argument('nTelefone', type=int)
    atributos.add_argument('dataAtualizacao', type=str)

    def get(self, cTelefone):
        telefone = TelefoneModel.find_telefone(cTelefone)
        if telefone:
            return telefone.json()
        raise TelefoneNaoExiste()
        #return {'menssagem': 'Telefone não foi encontrado.'}, 404

    def put(self, cTelefone):
        dados = Telefone.atributos.parse_args()
        dataAtualizacao = dados['dataAtualizacao']
        numerotel = dados['nTelefone']
        ddd = dados['cDDD']
        id_cliente = dados['cCliente']
        if len(str(ddd)) != 2:
            raise DDDInvalido()
            #return {"mensagem": "DDD do telefone invalido"}
        if len(str(numerotel)) != 9:
            raise NumeroInvalido()
            #return {"mensagem": "Numero de telefone invalido"}, 500
        if not ClienteModel.find_cliente(id_cliente):
            raise IdClienteNaoExiste()
            #return {"mensagem": "ID do Cliente não existe."}, 500
        if validar_data(dataAtualizacao) :
            telefone = TelefoneModel(cTelefone, **dados)
            telefone_encontrado = TelefoneModel.find_telefone(cTelefone)
            try:
                if telefone_encontrado:
                    telefone_encontrado.update_telefone(**dados)
                    telefone_encontrado.save_telefone()
                    return telefone_encontrado.json()

                    telefone.save_telefone()
            except:
                raise ErroInserir()
                #return {"mensagem": "Ocorreu um erro ao inserir o telefone. Verique a integridade"}, 500 #Internal Server Error
            return telefone.json(), 201
        else:
            raise DataInvalida()
            #return {"mensagem": "Data invalida."}, 500


    def delete(self, cTelefone):
        telefone = TelefoneModel.find_telefone(cTelefone)
        if telefone:
            telefone.delete_telefone()
            return {'messagem': 'telefone deletado.'}
        raise TelefoneNaoExiste()
        #return {'menssagem': 'telefone não encontrado.'}, 404
