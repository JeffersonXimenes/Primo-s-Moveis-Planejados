from flask_restful import Resource, reqparse
from models.ItensdoPedido_models import ItemPedidoModel
from models.vendas_models import VendasModel

class IdJaExiste(Exception):
    pass
class PedidoNaoExiste(Exception):
    pass
class ErroInserir(Exception):
    pass
class NaoExiste(Exception):
    pass

class Itens(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cItem', type=int)
    atributos.add_argument('cPedido', type=int)
    atributos.add_argument('iDescricao', type=str)

    def get(self):
        return {'Item Pedido: ': [item.json() for item in ItemPedidoModel.query.all()]}
    def post(self):
        dados = Itens.atributos.parse_args()
        id = dados['cItem']
        id_Pedido = dados['cPedido']
        if ItemPedidoModel.find_TipoPagamento(id):
            raise IdJaExiste()
        if not VendasModel.find_venda(id_Pedido):
            raise PedidoNaoExiste()

        item = ItemPedidoModel(**dados)
        try:
            item.save_Item()
        except:
            raise ErroInserir()
        return item.json()


class Item(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cPedido', type=int)
    atributos.add_argument('iDescricao', type=str)

    def get(self, cItem):
        item = ItemPedidoModel.find_Item(cItem)
        if item:
            return item.json()
        raise NaoExiste()
