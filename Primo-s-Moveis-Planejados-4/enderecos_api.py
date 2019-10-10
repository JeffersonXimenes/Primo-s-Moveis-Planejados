from flask import Blueprint, jsonify, request, render_template
from resources.endereco import Endereco,Enderecos, EnderecoNaoExiste, CepInvalido,\
UfInvalido,IdJaExiste,IdClienteNaoExiste,ErroInserir,DataInvalida
from infraestrutura.to_dict import to_dict, to_dict_list



enderecos_app = Blueprint('enderecos_app', __name__, template_folder='templates')

@enderecos_app.route("/cadastroEnderecos", methods=["GET"])
def login():
    return render_template("Cadastro_Clientes/CadastroEndereco.html")

@enderecos_app.route('/enderecos', methods=['GET'])
def listar():
    listar = Enderecos.get(Enderecos)
    return jsonify (to_dict(listar))

@enderecos_app.route('/enderecos/<int:id>', methods=['GET'])
def localizar(id):
    try:
        return jsonify(to_dict(Endereco.get(Endereco, id))), 200
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
def criar():

    cep = request.form["nCep"]   
    endereco = request.form["iEndereco"]
    complemento = request.form["iComplemento"]
    bairro = request.form["iBairro"]
    uf = request.form["iUf"]  

    enderecoCliente = {"cEndereco": 30,"cCliente":2, "nCep":cep,"iEndereco":endereco,"iComplemento": complemento, "iBairro":bairro, "iUf":uf}
    try:     
        criado = Enderecos.post(Enderecos, enderecoCliente)

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
def remover(id):
    try:
        removido = Endereco.delete(Endereco,id)
        return jsonify(to_dict(removido))
    except EnderecoNaoExiste:
        return 'menssagem: ID endereço não encontrado.'


