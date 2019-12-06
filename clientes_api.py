from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required
from infraestrutura.to_dict import to_dict, to_dict_list
from resources.cliente import Clientes, Cliente, ClienteNaoEncontrado, \
    CpfInvalido, ClienteJaCadastrado, DataInvalida, CpfJaCadastrado
from resources.endereco import  Enderecos, EnderecoNaoExiste, CepInvalido, \
    UfInvalido, IdJaExiste, IdClienteNaoExiste, ErroInserir
from infraestrutura.to_dict import to_dict, to_dict_list
from resources.telefone import  Telefones, TelefoneNaoExiste, DDDInvalido, \
    NumeroInvalido, IdJaExiste, IdClienteNaoExiste, ErroInserir

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

    cep = request.form["nCep"]
    endereco = request.form["iEndereco"]
    numero = request.form["numero"]
    complemento = request.form["iComplemento"]
    bairro = request.form["iBairro"]
    uf = request.form["cUf"]

    ddd = request.form["cDDD"]
    telefone = request.form["nTelefone"]

    try:
        criado = Clientes.post(Clientes)
        criarEndereco = Enderecos.post(Enderecos, criado['cCliente'])
        criarTelefone = Telefones.post(Telefones, criado['cCliente'])
        
        return render_template('Cadastro_Cliente_Sucesso.html')
    except CpfInvalido:
        return 'mensagem: CPF invalido.', 500
    except ClienteJaCadastrado:
        return 'mensagem: Cliente com ID ja cadastrado.', 500

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


@clientes_app.route('/clientes/<int:id>', methods=['DELETE'])
@login_required
def remover(id):
    try:
        Cliente.delete(Clientes,id)
        return " removido ",  200
    except:
        return " erro " , 404
