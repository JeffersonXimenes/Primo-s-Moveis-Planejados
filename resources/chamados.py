from flask_restful import Resource, reqparse
from models.chamados_models import ChamadoModel
from models.vendas_models import VendasModel
from infraestrutura.validacoes import validar_data

class VendaNaoExiste (Exception):
    pass
class IdJaExiste (Exception):
    pass
class ErroInserir (Exception):
    pass
class DataInvalida (Exception):
    pass
class ChamadoNaoExiste (Exception):
    pass

class Chamados(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cChamado', type=int)
    atributos.add_argument('cPedido', type=int)
    atributos.add_argument('movel', type=str)
    atributos.add_argument('tipoOcorrencia', type=str)
    atributos.add_argument('descricao', type=str)
    atributos.add_argument('dataAgendada', type=str)

    def get(self):
        return {'Chamados': [chamado.json() for chamado in ChamadoModel.query.all()]} # SELECT * FROM clientes

    def getID(self, cChamado):
        chamado = ChamadoModel.find_chamado(cChamado)
        if chamado:
            return chamado.json()
        raise ChamadoNaoExiste()

    def post(self):
        dados = Chamados.atributos.parse_args()
        id_chamado = dados['cChamado']
        id_venda = dados['cPedido']
        data = dados['dataAgendada']
        if ChamadoModel.find_chamado(id_chamado):
            raise IdJaExiste()

        if not VendasModel.find_venda(id_venda):
            raise VendaNaoExiste()

        if validar_data(data):
            chamado = ChamadoModel(**dados)
            try:
                chamado.save_chamado()
            except:
                raise ErroInserir()

            return chamado.json()
        else:
            raise DataInvalida()

    def delete(self, cChamado):
        chamado = ChamadoModel.find_chamado(cChamado)
        if chamado:
            chamado.delete_chamado()
            return {'messagem': 'chamado deletado.'}
        raise ChamadoNaoExiste()



