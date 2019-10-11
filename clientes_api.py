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
    dataCadastro = request.form["dataCadastro"]
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
    except ClienteJaCadastrado:
        return 'mensagem: Cliente com ID ja cadastrado.', 500
    except DataInvalida:
        return 'mensagem: Data invalida.', 500
    except CpfJaCadastrado:
        return 'mensagem: CPF ja cadastrado.', 500

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
'''
        id_cliente = str(criado['cCliente'])
        print(id_cliente,"id_cliente")
        dadosEndereco =  {"cEndereco": id, "cCliente": id_cliente, "nCep": cep, "iEndereco": endereco,"iComplemento": complemento, "iBairro": bairro, "cUf": uf,"dataAtualizacao":dataAtualizacao}
        print(dadosEndereco,"dados endereco")
        criadoEndereco = Enderecos.post(Enderecos,dadosEndereco)
        #print(criadoEndereco, "criado endereco" , criado,"criados pessoa")
        



'''
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

