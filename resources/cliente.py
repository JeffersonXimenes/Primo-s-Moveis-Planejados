from flask_restful import Resource, reqparse
from models.clientes import ClienteModel

class Clientes(Resource):
    def get(self):
        return {'clientes': [cliente.json() for cliente in ClienteModel.query.all()]} # SELECT * FROM clientes

class Cliente(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nCpf', type=str, required=True, help="The field 'nome' cannot be left blank.")
    atributos.add_argument('nome')
    atributos.add_argument('dataNascimento')
    atributos.add_argument('dataCadastro')

    def get(self, cCliente):
        cliente = ClienteModel.find_cliente(cCliente)
        if cliente:
            return cliente.json()
        return {'menssagem': 'Cliente não foi encontrado.'}, 404

    def post(self, cCliente):
        if ClienteModel.find_cliente(cCliente):
            return {"menssagem": "Cliente id '{}' não existe.".format(cCliente)}, 400 #Bad Request

        dados = Cliente.atributos.parse_args()
        cliente = ClienteModel(cCliente, **dados)
        try:
            cliente.save_cliente()
        except:
            return {"mensagem": "Ocorreu um erro ao inserir o cliente."}, 500 #Internal Server Error
        return cliente.json(), 201

    def put(self, cCliente):
        dados = Cliente.atributos.parse_args()
        cliente = ClienteModel(cCliente, **dados)

        cliente_encontrado = ClienteModel.find_cliente(cCliente)
        if cliente_encontrado:
            cliente_encontrado.update_cliente(**dados)
            cliente_encontrado.save_cliente()
            return cliente_encontrado.json(), 200
        cliente.save_cliente()
        return cliente.json(), 201

    def delete(self, cCliente):
        cliente = ClienteModel.find_cliente(cCliente)
        if cliente:
            cliente.delete_cliente()
            return {'messagem': 'Cliente deletado.'}
        return {'menssagem': 'Cliente não encontrado.'}, 404
