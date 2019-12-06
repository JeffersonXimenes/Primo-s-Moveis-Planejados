from flask_restful import Resource, reqparse
from models.vendas_models import VendasModel
from models.clientes import ClienteModel
from infraestrutura.validacoes import validar_data
from models.clientes import ClienteModel
from models.funcionario_models import FuncionarioModel
from models.tipoPagamento_models import TipoPagamentoModel
import json

class IdJaExiste(Exception):
    pass


class IdClienteNaoExiste(Exception):
    pass


class DataInvalida(Exception):
    pass


class IdFuncNaoExiste(Exception):
    pass


class ErroInserir(Exception):
    pass


class VendaNaoExiste(Exception):
    pass


class TipoNaoExiste(Exception):
    pass

class JoinVendas(Resource):
    def getJoin():        
    
        return VendasModel.join_clientes()    

class Vendas(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cPedido', type=int)
    atributos.add_argument('cCliente', type=int)
    atributos.add_argument('cFuncionario', type=int)
    atributos.add_argument('dataVenda', type=str)
    atributos.add_argument('nContrato', type=str)
    atributos.add_argument('iTipoContrato', type=str)
    atributos.add_argument('cTipoPagamento', type=int)

    def get(self):
        return {'vendas': [venda.json() for venda in VendasModel.query.all()]}  # SELECT * FROM clientes    

    def post(self, dadosCPF, dadosFunc):
        dados = Vendas.atributos.parse_args()
        id = dados['cPedido']
        dataVenda = dados['dataVenda']
        id_cliente = ClienteModel.find_ID(dadosCPF)
        dados['cCliente'] = id_cliente
        id_tipo = dados['cTipoPagamento']
        id_func = FuncionarioModel.find_ID_Matricula(dadosFunc)
        dados['cFuncionario'] = id_func
        if VendasModel.find_venda(id):
            raise IdJaExiste()
        if not ClienteModel.find_cliente(id_cliente):
            raise IdClienteNaoExiste()
        if not FuncionarioModel.find_funcionario(id_func):
            raise IdFuncNaoExiste()
        if not TipoPagamentoModel.find_TipoPagamento(id_tipo):
            raise TipoNaoExiste()
        if validar_data(dataVenda):
            venda = VendasModel(**dados)
            try:
                venda.save_venda()
            except:
                raise ErroInserir()

            return venda.json()
        else:
            raise DataInvalida()


class Venda(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cCliente', type=int)
    atributos.add_argument('cFuncionario', type=int)
    atributos.add_argument('dataVenda', type=str)
    atributos.add_argument('nContrato', type=str)
    atributos.add_argument('iTipoContrato', type=str)
    atributos.add_argument('cTipoPagamento', type=int)

    def get(self, cPedido):
        venda = VendasModel.find_venda(cPedido)
        if venda:
            return venda.json()
        raise VendaNaoExiste()

    def put(self, cPedido):
        dados = Venda.atributos.parse_args()
        dataVenda = dados['dataVenda']
        id_cliente = dados['cCliente']
        id_tipo = dados['cTipoPagamento']
        id_func = dados['cFuncionario']

        if not ClienteModel.find_cliente(id_cliente):
            raise IdClienteNaoExiste()
        if not TipoPagamentoModel.find_TipoPagamento(id_tipo):
            raise TipoNaoExiste()
        if not FuncionarioModel.find_funcionario(id_func):
            raise IdFuncNaoExiste()
        if validar_data(dataVenda):
            venda = VendasModel(cPedido, **dados)
            venda_encontrado = VendasModel.find_venda(cPedido)
            try:
                if venda_encontrado:
                    venda_encontrado.update_venda(**dados)
                    venda_encontrado.save_venda()
                    return venda_encontrado.json()

                venda.save_telefone()
            except:
                raise ErroInserir()

            return venda.json()
        else:
            raise DataInvalida()

    def delete(self, cPedido):
        venda = VendasModel.find_venda(cPedido)
        if venda:
            venda.delete_venda()
            return {'messagem': 'venda deletada.'}
        raise VendaNaoExiste()