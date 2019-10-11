from flask import Blueprint, jsonify, request, render_template
from infraestrutura.to_dict import to_dict, to_dict_list
from resources.cliente import Clientes,Cliente, ClienteNaoEncontrado,\
    CpfInvalido, ClienteJaCadastrado,DataInvalida,CpfJaCadastrado
from resources.endereco import Endereco,Enderecos, EnderecoNaoExiste, CepInvalido,\
UfInvalido,IdJaExiste,IdClienteNaoExiste,ErroInserir,DataInvalida
from infraestrutura.to_dict import to_dict, to_dict_list
from resources.telefone import Telefone,Telefones, TelefoneNaoExiste, DDDInvalido,\
NumeroInvalido,IdJaExiste,IdClienteNaoExiste,ErroInserir,DataInvalida


clientes_app = Blueprint('clientes_app', __name__, template_folder='templates')

@clientes_app.route("/cadastro", methods=["GET"])
def login():
    return render_template("CadastroClientes.html")

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
    dataCadastro = request.form["dataAtualizacao"]
    dados = {"nCpf": cpf, "iNome": nome,"iEmail":email,"dataNascimento":dataNascimento,"dataCadastro":dataCadastro}

    cep = request.form["nCep"]
    endereco = request.form["iEndereco"]
    complemento = request.form["iComplemento"]
    bairro = request.form["iBairro"]
    uf = request.form["cUf"]
    dataAtualizacao = request.form["dataAtualizacao"]

    ddd = request.form["cDDD"]
    telefone = request.form["nTelefone"]

#{"nCpf":"47932819822", "iNome":"Joao","iEmail":"joao@jo","dataNascimento":"26/09/2019","dataCadastro":"11/10/2019"}

    try:
        criado = Clientes.post(Clientes)
        dadosEndereco = {"cEndereco":criado['cCliente'], "cCliente": criado['cCliente'], "nCep": cep, "iEndereco": endereco, "iComplemento": complemento,"iBairro": bairro, "cUf": uf, "dataAtualizacao": dataAtualizacao}
        criarEndereco = Enderecos.post(Enderecos,dadosEndereco)
        dadosTelefone = {"cTelefone":criado['cCliente'],"cCliente": criado['cCliente'],"cDDD":ddd,"nTelefone":telefone,"dataAtualizacao": dataAtualizacao }
        criarTelefone = Telefones.post(Telefones,dadosTelefone)
        return 'criado', 201
    except CpfInvalido:
        return 'mensagem: CPF invalido.', 500