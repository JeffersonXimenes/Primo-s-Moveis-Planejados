from flask_restful import Resource, reqparse
from models.endereco_models import EnderecoModel
from infraestrutura.validacoes import validar_data
from models.clientes import ClienteModel

class CepInvalido (Exception):
    pass
class UfInvalido (Exception):
    pass

class IdJaExiste (Exception):
    pass
class IdClienteNaoExiste (Exception):
    pass
class ErroInserir (Exception):
    pass
class DataInvalida (Exception):
    pass
class EnderecoNaoExiste (Exception):
    pass

class Enderecos(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cEndereco', type=int)
    atributos.add_argument('cCliente', type=int)
    atributos.add_argument('nCep', type=str)
    atributos.add_argument('iEndereco', type=str)
    atributos.add_argument('numero', type=str)
    atributos.add_argument('iComplemento', type=str)
    atributos.add_argument('iBairro', type=str)
    atributos.add_argument('cUf', type=str)


    def get(self):
        return {'endereços': [endereco.json() for endereco in EnderecoModel.query.all()]} # SELECT * FROM clientes
    def post(self,cod_cliente):
        dados = Enderecos.atributos.parse_args()
        id = dados['cEndereco']
        dados['cCliente'] = cod_cliente
        id_cliente = cod_cliente
        cep = dados['nCep']
        uf = dados['cUf']
        if len(str(cep)) != 9:
            raise CepInvalido()
            #return {"mensagem": "DDD do telefone invalido"}
        if len(str(uf)) != 2:
            raise UfInvalido()
            #return {"mensagem": "Numero de telefone invalido"}, 500
        if EnderecoModel.find_endereco(id):
            raise IdJaExiste()
            #return {"menssagem": "Telefone id '{}' já existe.".format(id)}, 400 #Bad Request
        if not ClienteModel.find_cliente(id_cliente):
            raise IdClienteNaoExiste()
            #return {"mensagem": "ID do Cliente não existe."}, 500

        endereco = EnderecoModel(**dados)
        try:
            endereco.save_endereco()
        except:
            raise ErroInserir()
            #return {"mensagem": "Ocorreu um erro ao inserir o telefone."}, 500 #Internal Server Error
        return endereco.json()


class Endereco(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cCliente', type=int)
    atributos.add_argument('nCep', type=str)
    atributos.add_argument('iEndereco', type=str)
    atributos.add_argument('numero', type=str)
    atributos.add_argument('iComplemento', type=str)
    atributos.add_argument('iBairro', type=str)
    atributos.add_argument('cUf', type=str)
    atributos.add_argument('dataAtualizacao', type=str)

    def get(self, cEndereco):
        endereco = EnderecoModel.find_endereco(cEndereco)
        if endereco:
            return endereco.json()
        raise EnderecoNaoExiste()
        #return {'menssagem': 'Telefone não foi encontrado.'}, 404

    def put(self, cEndereco):
        dados = Endereco.atributos.parse_args()
        dataAtualizacao = dados['dataAtualizacao']
        id_cliente = dados['cCliente']
        cep = dados['nCep']
        uf = dados['cUf']
        if len(str(cep)) != 8:
            raise CepInvalido()
            #return {"mensagem": "DDD do telefone invalido"}
        if len(str(uf)) != 2:
            raise UfInvalido()
            #return {"mensagem": "Numero de telefone invalido"}, 500
        if not ClienteModel.find_cliente(id_cliente):
            raise IdClienteNaoExiste()
            #return {"mensagem": "ID do Cliente não existe."}, 500

            endereco = EnderecoModel(cEndereco, **dados)
            endereco_encontrado = EnderecoModel.find_endereco(cEndereco)
            try:
                if endereco_encontrado:
                    endereco_encontrado.update_endereco(**dados)
                    endereco_encontrado.save_telefone()
                    return endereco_encontrado.json()

                    endereco.save_endereco()
            except:
                raise ErroInserir()
                #return {"mensagem": "Ocorreu um erro ao inserir o telefone. Verique a integridade"}, 500 #Internal Server Error
            return endereco.json(), 201


    def delete(self, cEndereco):
        endereco = EnderecoModel.find_endereco(cEndereco)
        if endereco:
            endereco.delete_endereco()
            return {'messagem': 'endereco deletado.'}
        raise EnderecoNaoExiste()
        #return {'menssagem': 'telefone não encontrado.'}, 404
