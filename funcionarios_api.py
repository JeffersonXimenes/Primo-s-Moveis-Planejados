from flask import Blueprint, jsonify, request
from resources.funcionario import Funcionario,Funcionarios, CpfInvalido, FuncionarioNaoExiste,IdJaExiste,\
    DataInvalida,CargoNaoExiste,ErroInserir
from infraestrutura.to_dict import to_dict, to_dict_list


funcionarios_app = Blueprint('funcionarios_app', __name__, template_folder='templates')


@funcionarios_app.route('/funcionarios', methods=['GET'])
def listar():
    listar = Funcionarios.get(Funcionarios)
    return jsonify (listar)

@funcionarios_app.route('/funcionarios/<int:id>', methods=['GET'])
def localizar(id):
    try:
        return jsonify(to_dict(Funcionario.get(Funcionario,id))), 200
    except FuncionarioNaoExiste:
        return 'menssagem: O funcionario não foi encontrado.', 404

@funcionarios_app.route('/funcionarios', methods=['POST'])
def criar():
    try:
        criado = Funcionarios.post(Funcionarios)
        return jsonify (to_dict(criado)), 201
    except IdJaExiste:
        return  "mensagem:Id do funcionario já existe.", 500
    except DataInvalida:
        return "mensagem: Data invalida.", 500
    except CpfInvalido:
        return "mensagem: Cpf do funcionario invalido", 500
    except CargoNaoExiste:
        return "mensagem: Cargo do funcionario não encontrado.", 404
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o funcionario, verifique a integridade.", 500


@funcionarios_app.route('/funcionarios/<int:id>', methods=['PUT'])
def atualizar(id):
    try:
        atualizado = Funcionario.put(Funcionario,id)
        return jsonify(to_dict(atualizado)), 201
    except CargoNaoExiste:
        return "mensagem: Cargo do funcionario não encontrado.", 404
    except DataInvalida:
        return 'mensagem: Data invalida.', 500
    except CpfInvalido:
        return "mensagem: Cpf do funcionario invalido", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o funcionario. Verique a integridade"


@funcionarios_app.route('/funcionarios/<int:id>', methods=['DELETE'])
def remover(id):
    try:
        removido = Funcionario.delete(Funcionario,id)
        return jsonify(to_dict(removido)) , 200
    except FuncionarioNaoExiste:
        return 'menssagem: Funcionario não encontrado.'


