from flask import Blueprint, jsonify, request, render_template
from infraestrutura.to_dict import to_dict, to_dict_list
from resources.cliente import Clientes,Cliente, ClienteNaoEncontrado,\
    CpfInvalido, ClienteJaCadastrado,DataInvalida,CpfJaCadastrado



clientes_app = Blueprint('clientes_app', __name__, template_folder='templates')

@clientes_app.route("/cadastro", methods=["GET"])
def login():
    return render_template("login.html", mensagem="Cadastre o cliente")

@clientes_app.route('/clientes', methods=['GET'])
def listar():
    listar = Clientes.get(Clientes)
    return jsonify (listar)

@clientes_app.route('/clientes/<int:id>', methods=['GET'])
def localizar(id):
    try:
        return jsonify(to_dict(Cliente.get(Cliente,id))), 200
    except ClienteNaoEncontrado:
        return 'menssagem: Cliente não foi encontrado.', 404

@clientes_app.route('/clientes', methods=['POST','GET'] )
def criar():
    #id = request.form["cCliente"]
    cpf = request.form["nCpf"]
    nome = request.form["iNome"]
    email = request.form["iEmail"]
    dataNascimento = request.form["dataNascimento"]
    dataCadastro = request.form["dataCadastro"]
    dados = {"cCliente":id,"nCpf": cpf, "iNome": nome,"iEmail":email,"dataNascimento":dataNascimento,"dataCadastro":dataCadastro}
    print(dados,"1")
    try:
        criado = Clientes.post(Clientes,dados)
        print (jsonify((to_dict_list(criado),"2")))
        return jsonify(to_dict(criado)) , 201
    except CpfInvalido:
        return 'mensagem: CPF invalido.', 500
    except ClienteJaCadastrado:
        return 'mensagem: Cliente com ID ja cadastrado.', 500
    except DataInvalida:
        return 'mensagem: Data invalida.', 500
    except CpfJaCadastrado:
        return 'mensagem: CPF ja cadastrado.', 500

@clientes_app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar(id):
    try:
        atualizado = Cliente.put(Cliente,id), 201
        return jsonify(to_dict(atualizado)), 201
    except CpfInvalido:
        return 'mensagem: CPF invalido.', 500
    except DataInvalida:
        return 'mensagem: Data invalida.', 500
    except CpfJaCadastrado:
        return 'mensagem: Ocorreu um erro ao atualizar o cliente, CPF de outro cliente.', 500
    except ClienteNaoEncontrado:
        return 'mensagem: Cliente não encontrado.', 500

'''
@clientes_app.route('/alunos/<int:id>', methods=['DELETE'])
def remover(id):
    try:
        removido = service_remover(id)
    except AlunoAtreladoASolicitacaoMatricula:
        return 'Aluno atrelado a uma solicitação de matricula', 422
    if removido != None:
        return jsonify(to_dict(removido))
    return , 404
'''

