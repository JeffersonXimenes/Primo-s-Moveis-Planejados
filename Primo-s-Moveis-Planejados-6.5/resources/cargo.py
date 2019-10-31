from flask_restful import Resource, reqparse
from models.cargo_models import CargoModel


class IdJaExiste (Exception):
    pass
class ErroInserir (Exception):
    pass
class CargoNaoExiste (Exception):
    pass

class Cargos(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('cCargos', type=int)
    atributos.add_argument('iCargos', type=str)


    def get(self):
        return {'cargos': [cargo.json() for cargo in CargoModel.query.all()]} # SELECT * FROM clientes
    def post(self):
        dados = Cargos.atributos.parse_args()
        id = dados['cCargos']
        if CargoModel.find_cargo(id):
            raise IdJaExiste()
            #return {"menssagem": "Telefone id '{}' já existe.".format(id)}, 400 #Bad Request
        cargo = CargoModel(**dados)
        try:
            cargo.save_cargo()
        except:
            raise ErroInserir()
        return cargo.json()
                #return {"mensagem": "Ocorreu um erro ao inserir o telefone."}, 500 #Internal Server Error

class Cargo(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('iCargos', type=str)

    def get(self, cCargos):
        cargo = CargoModel.find_cargo(cCargos)
        if cargo:
            return cargo.json()
        raise CargoNaoExiste()
        #return {'menssagem': 'Telefone não foi encontrado.'}, 404

    def put(self, cCargos):
        dados = Cargo.atributos.parse_args()
        cargo = CargoModel(cCargos, **dados)
        cargo_encontrado = CargoModel.find_cargo(cCargos)

        try:
            if cargo_encontrado:
                cargo_encontrado.update_cargo(**dados)
                cargo_encontrado.save_cargo()

                return cargo_encontrado.json()
            cargo.save_cargo()
        except:
            raise ErroInserir()
            #return {"mensagem": "Ocorreu um erro ao inserir o telefone. Verique a integridade"}, 500 #Internal Server Error
        return cargo.json()



    def delete(self, cCargos):
        cargo = CargoModel.find_cargo(cCargos)
        if cargo:
            cargo.delete_cargo()
            return {'messagem': 'cargo deletado.'}
        raise CargoNaoExiste()
        #return {'menssagem': 'telefone não encontrado.'}, 404
