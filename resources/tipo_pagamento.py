from flask_restful import Resource, reqparse
from models.tipoPagamento_models import TipoPagamentoModel

class IdJaExiste (Exception):
    pass
class ErroInserir (Exception):
    pass
class TipoNaoExiste (Exception):
    pass

class TipoPagamentos(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cTipoPagamento', type=int)
    atributos.add_argument('nParcelas', type=int)
    atributos.add_argument('Formapagamento', type=str)


    def get(self):
        return {'tipo_pagamento': [pagamento.json() for pagamento in TipoPagamentoModel.query.all()]} # SELECT * FROM clientes
    def post(self):
        dados = TipoPagamentos.atributos.parse_args()
        id = dados['cTipoPagamento']
        if TipoPagamentoModel.find_TipoPagamento(id):
            raise IdJaExiste()

        pagamento = TipoPagamentoModel(**dados)
        try:
            pagamento.save_TipoPagamento()
        except:
            raise ErroInserir()
        return pagamento.json()


class TipoPagamento(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nParcelas', type=int)
    atributos.add_argument('Formapagamento', type=str)

    def get(self, cTipoPagamento):
        pagamento = TipoPagamentoModel.find_TipoPagamento(cTipoPagamento)
        if pagamento:
            return pagamento.json()
        raise TipoNaoExiste()

    def put(self, cTipoPagamento):
        dados = TipoPagamento.atributos.parse_args()
        pagamento = TipoPagamentoModel(cTipoPagamento, **dados)
        pagamento_encontrado = TipoPagamentoModel.find_TipoPagamento(cTipoPagamento)

        try:
            if pagamento_encontrado:
                pagamento_encontrado.update_TipoPagamento(**dados)
                pagamento_encontrado.save_TipoPagamento()

                return pagamento_encontrado.json()
            pagamento.save_cargo()
        except:
            raise ErroInserir()

        return pagamento.json()



    def delete(self, cTipoPagamento):
        pagamento = TipoPagamentoModel.find_TipoPagamento(cTipoPagamento)
        if pagamento:
            pagamento.delete_TipoPagamento()
            return {'messagem': 'Tipo de pagamento deletado.'}
        raise TipoNaoExiste()

