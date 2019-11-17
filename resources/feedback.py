from flask_restful import Resource, reqparse
from models.feedback_models import FeedbackModel
from infraestrutura.validacoes import validar_data
from models.vendas_models import VendasModel



class IdJaExiste (Exception):
    pass
class VendaNaoExiste(Exception):
    pass

class ErroInserir(Exception):
    pass
class NaoExiste(Exception):
    pass


class Feedbacks(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cFeedback', type=int)
    atributos.add_argument('ambiente', type=str)
    atributos.add_argument('notaAtendimento', type=int)
    atributos.add_argument('notaVendedor', type=int)
    atributos.add_argument('notaMontagem', type=int)
    atributos.add_argument('mensagem', type=str)
    atributos.add_argument('cPedido', type=int)

    def get(self):
        return {'Feedback': [feed.json() for feed in FeedbackModel.query.all()]} # SELECT * FROM clientes

    def post(self):
        dados = Feedbacks.atributos.parse_args()
        id = dados['cFeedback']
        id_pedido = dados['cPedido']
        if FeedbackModel.find_feed(id):
            raise IdJaExiste()
        if not VendasModel.find_venda(id_pedido):
            raise VendaNaoExiste()

        feed = FeedbackModel(**dados)
        try:
            feed.save_feed()
        except:
            raise ErroInserir()
        return feed.json()


    def getID(self, cFeedback):
        feed = FeedbackModel.find_feed(cFeedback)
        if feed:
            return feed.json()
        raise NaoExiste()
