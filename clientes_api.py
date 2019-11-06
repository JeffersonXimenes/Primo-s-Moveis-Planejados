from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required
from infraestrutura.to_dict import to_dict, to_dict_list
from resources.cliente import Clientes, Cliente, ClienteNaoEncontrado, \
    CpfInvalido, ClienteJaCadastrado, DataInvalida, CpfJaCadastrado
from resources.endereco import  Enderecos, EnderecoNaoExiste, CepInvalido, \
    UfInvalido, IdJaExiste, IdClienteNaoExiste, ErroInserir, DataInvalida
from infraestrutura.to_dict import to_dict, to_dict_list
from resources.telefone import  Telefones, TelefoneNaoExiste, DDDInvalido, \
    NumeroInvalido, IdJaExiste, IdClienteNaoExiste, ErroInserir, DataInvalida

clientes_app = Blueprint('clientes_app', __name__, template_folder='templates')

'''
@clientes_app.route("/cadastro", methods=["GET"])
def login():
    return render_template("CadastroClientes.html")
'''

@clientes_app.route('/allclientes')
def paginainicial():
    return render_template('getClientes.html')

@clientes_app.route('/clientes', methods=['GET'])
@login_required
def listar():
    data = Clientes.get(Clientes)
    return jsonify(data)


@clientes_app.route('/clientes/<int:id>', methods=['GET'])
@login_required
def localizar(id):
    try:
        return jsonify(to_dict(Cliente.get(Cliente, id))), 200
    except ClienteNaoEncontrado:
        return 'menssagem: Cliente não foi encontrado.', 404


@clientes_app.route('/clientes', methods=['POST'])
@login_required
def criar():
    # id = request.form["cCliente"]
    cpf = request.form["nCpf"]
    nome = request.form["iNome"]
    email = request.form["iEmail"]
    dataNascimento = request.form["dataNascimento"]
    dataCadastro = request.form["dataCadastro"]
    dados = {"nCpf": cpf, "iNome": nome, "iEmail": email, "dataNascimento": dataNascimento,
             "dataCadastro": dataCadastro}

    cep = request.form["nCep"]
    endereco = request.form["iEndereco"]
    numero = request.form["numero"]
    complemento = request.form["iComplemento"]
    bairro = request.form["iBairro"]
    uf = request.form["cUf"]
    dataAtualizacao = request.form["dataAtualizacao"]

    ddd = request.form["cDDD"]
    telefone = request.form["nTelefone"]

    # {"nCpf":"47932819822", "iNome":"Joao","iEmail":"joao@jo","dataNascimento":"26/09/2019","dataCadastro":"11/10/2019"}

    try:
        criado = Clientes.post(Clientes)
        dadosEndereco = {"cEndereco": criado['cCliente'], "cCliente": criado['cCliente'], "nCep": cep,
                         "iEndereco": endereco, "numero":numero,"iComplemento": complemento, "iBairro": bairro, "cUf": uf,
                         "dataAtualizacao": dataAtualizacao}
        criarEndereco = Enderecos.post(Enderecos, dadosEndereco)
        dadosTelefone = {"cTelefone": criado['cCliente'], "cCliente": criado['cCliente'], "cDDD": ddd,
                         "nTelefone": telefone, "dataAtualizacao": dataAtualizacao}
        criarTelefone = Telefones.post(Telefones, dadosTelefone)
        return 'Cliente cadastrado com sucesso', 201
    except CpfInvalido:
        return 'mensagem: CPF invalido.', 500
    except ClienteJaCadastrado:
        return 'mensagem: Cliente com ID ja cadastrado.', 500
    except DataInvalida:
        return 'mensagem: Data invalida.', 500
    except CpfJaCadastrado:
        return 'mensagem: CPF ja cadastrado.', 500

    except CepInvalido:
        return "mensagem: CEP do endereço invalido", 500
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

    except DDDInvalido:
        return "mensagem: DDD do telefone invalido", 500
    except NumeroInvalido:
        return "mensagem: Numero de telefone invalido", 500
    except IdJaExiste:
        return "menssagem: ID Telefone  já existe.", 400
    except IdClienteNaoExiste:
        return "mensagem: Cliente não encontrado.", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o telefone.", 500



