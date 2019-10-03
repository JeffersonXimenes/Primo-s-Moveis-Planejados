from flask import Blueprint, jsonify, request
from resources.telefone import Telefone,Telefones, TelefoneNaoExiste, DDDInvalido,\
NumeroInvalido,IdJaExiste,IdClienteNaoExiste,ErroInserir,DataInvalida
from infraestrutura.to_dict import to_dict, to_dict_list


telefones_app = Blueprint('telefones_app', __name__, template_folder='templates')


@telefones_app.route('/telefones', methods=['GET'])
def listar():
    listar = Telefones.get(Telefones)
    return jsonify (listar)

@telefones_app.route('/telefones/<int:id>', methods=['GET'])
def localizar(id):
    try:
        return jsonify(to_dict(Telefone.get(Telefone,id))), 200
    except TelefoneNaoExiste:
        return 'menssagem: Telefone não foi encontrado.', 404
'''
@clientes_app.route('/clientes/<int:id>', methods=['GET'])
def localizar(id):
    verificaCliente = Cliente.get(Cliente,id)
    if verificaCliente == 0:
        return 'menssagem: Cliente não foi encontrado.', 404
    return jsonify(to_dict(Cliente.get(Cliente,id))), 200
'''

@telefones_app.route('/telefones', methods=['POST'])
def criar():
    try:
        criado = Telefones.post(Telefones), 201
        return jsonify(criado)
    except DDDInvalido:
        return  "mensagem: DDD do telefone invalido", 500
    except NumeroInvalido:
        return "mensagem: Numero de telefone invalido", 500
    except IdJaExiste:
        return "menssagem: ID Telefone  já existe.", 400
    except IdClienteNaoExiste:
        return "mensagem: Cliente não encontrado.", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o telefone.", 500
    except DataInvalida:
        return "mensagem: Data invalida.", 500

@telefones_app.route('/telefones/<int:id>', methods=['PUT'])
def atualizar(id):
    try:
        atualizado = Telefone.put(Telefone,id)
        return jsonify(to_dict(atualizado)), 201
    except DDDInvalido:
        return "mensagem: DDD do telefone invalido", 500
    except DataInvalida:
        return 'mensagem: Data invalida.', 500
    except NumeroInvalido:
        return "mensagem: Numero de telefone invalido", 500
    except IdClienteNaoExiste:
        return 'mensagem: Cliente não encontrado.', 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o telefone. Verique a integridade"


@telefones_app.route('/telefones/<int:id>', methods=['DELETE'])
def remover(id):
    try:
        removido = Telefone.delete(Telefone,id)
        return jsonify(to_dict(removido))
    except TelefoneNaoExiste:
        return 'menssagem: telefone não encontrado.'


