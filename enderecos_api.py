from flask import Blueprint, jsonify, request
from flask_login import login_required
from resources.endereco import Endereco,Enderecos, EnderecoNaoExiste, CepInvalido,\
UfInvalido,IdJaExiste,IdClienteNaoExiste,ErroInserir,DataInvalida
from infraestrutura.to_dict import to_dict, to_dict_list


enderecos_app = Blueprint('enderecos_app', __name__, template_folder='templates')


@enderecos_app.route('/enderecos', methods=['GET'])
@login_required
def listar():
    listar = Enderecos.get(Enderecos)
    return jsonify (listar)

@enderecos_app.route('/enderecos/<int:id>', methods=['GET'])
@login_required
def localizar(id):
    try:
        return jsonify(Endereco.get(Endereco,id)), 200
    except EnderecoNaoExiste:
        return 'menssagem: ID Endereço não foi encontrado.', 404
'''
@clientes_app.route('/clientes/<int:id>', methods=['GET'])
def localizar(id):
    verificaCliente = Cliente.get(Cliente,id)
    if verificaCliente == 0:
        return 'menssagem: Cliente não foi encontrado.', 404
    return jsonify(to_dict(Cliente.get(Cliente,id))), 200
'''

@enderecos_app.route('/enderecos', methods=['POST'])
@login_required
def criar():
    try:
        criado = Enderecos.post(Enderecos)
        return jsonify (to_dict(criado)), 201
    except CepInvalido:
        return  "mensagem: CEP do endereço invalido", 500
    except UfInvalido:
        return "mensagem: Uf do endereço invalido", 500
    except IdJaExiste:
        return "menssagem: ID endereço  já existe.", 400
    except IdClienteNaoExiste:
        return "mensagem: Cliente não encontrado.", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o endereco.", 500
    except DataInvalida:
        return "mensagem: Data invalida.", 500

@enderecos_app.route('/enderecos/<int:id>', methods=['PUT'])
@login_required
def atualizar(id):
    try:
        atualizado = Endereco.put(Endereco,id)
        return jsonify(to_dict(atualizado)), 201
    except CepInvalido:
        return "mensagem: CEP do endereço invalido", 500
    except DataInvalida:
        return 'mensagem: Data invalida.', 500
    except UfInvalido:
        return "mensagem:  Uf do endereço invalido", 500
    except IdClienteNaoExiste:
        return 'mensagem: Cliente não encontrado.', 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o telefone. Verique a integridade"


@enderecos_app.route('/enderecos/<int:id>', methods=['DELETE'])
@login_required
def remover(id):
    try:
        removido = Endereco.delete(Endereco,id)
        return jsonify(removido)
    except EnderecoNaoExiste:
        return 'menssagem: ID endereço não encontrado.'


