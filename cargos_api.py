from flask import Blueprint, jsonify, request
from resources.cargo import Cargo, Cargos, CargoNaoExiste,IdJaExiste, ErroInserir
from infraestrutura.to_dict import to_dict, to_dict_list


cargo_app = Blueprint('cargo_app', __name__, template_folder='templates')


@cargo_app.route('/cargos', methods=['GET'])
def listar():
    listar = Cargos.get(Cargos)
    return jsonify (listar)

@cargo_app.route('/cargos/<int:id>', methods=['GET'])
def localizar(id):
    try:
        return jsonify(to_dict(Cargo.get(Cargo,id))), 200
    except CargoNaoExiste:
        return 'menssagem: O cargo não foi encontrado.', 404
'''
@clientes_app.route('/clientes/<int:id>', methods=['GET'])
def localizar(id):
    verificaCliente = Cliente.get(Cliente,id)
    if verificaCliente == 0:
        return 'menssagem: Cliente não foi encontrado.', 404
    return jsonify(to_dict(Cliente.get(Cliente,id))), 200
'''

@cargo_app.route('/cargos', methods=['POST'])
def criar():
    try:
        criado = Cargos.post(Cargos)
        return jsonify (to_dict(criado)), 201
    except IdJaExiste:
        return  "mensagem:Id do cargo já existe", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o cargo.", 500

@cargo_app.route('/cargos/<int:id>', methods=['PUT'])
def atualizar(id):
    try:
        atualizado = Cargo.put(Cargo,id)
        return jsonify(to_dict(atualizado)), 201
    except IdJaExiste:
        return "mensagem:Id do cargo já existe", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o cargo.", 500



@cargo_app.route('/cargos/<int:id>', methods=['DELETE'])
def remover(id):
    try:
        removido = Cargo.delete(Cargo,id)
        return jsonify(to_dict(removido))
    except CargoNaoExiste:
        return 'menssagem: cargo não encontrado.'


