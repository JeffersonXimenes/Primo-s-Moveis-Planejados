from flask_restful import Resource, reqparse
from models.acompanhamentoPedido import AcompanhamentoPedidoModel
from infraestrutura.validacoes import validar_data
from models.funcionario_models import FuncionarioModel
from models.vendas_models import VendasModel

class AcompanhamentoNaoExiste(Exception):
    pass
class IdFuncNaoExiste(Exception):
    pass
class IdVendaNaoExiste(Exception):
    pass
class DataInvalida(Exception):
    pass
class ErroInserir(Exception):
    pass

class AcompanhamentoPedido(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cAcompanhamento', type=int)
    atributos.add_argument('iDescricao', type=str)
    atributos.add_argument('cFuncionario', type=int)
    atributos.add_argument('cPedido', type=int)

    def get(self):
        return {'acompanhamentos': [acompanhamento.json() for acompanhamento in AcompanhamentoPedidoModel.query.all()]}
    def post(self, matricula_func):
        dados = AcompanhamentoPedido.atributos.parse_args()
        id_funcionario = FuncionarioModel.find_ID_Matricula(matricula_func)
        dados['cFuncionario'] = id_funcionario
        id_pedido = dados['cPedido']

        if not FuncionarioModel.find_funcionario(id_funcionario):
            raise IdFuncNaoExiste()

        if not VendasModel.find_venda(id_pedido):
            raise IdVendaNaoExiste()


        acompanhamento = AcompanhamentoPedidoModel(**dados)
        try:
            acompanhamento.save_acompanhamento()
        except:
            ErroInserir()


