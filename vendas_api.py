from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required
from resources.venda import Venda,Vendas,IdJaExiste,IdClienteNaoExiste,\
    DataInvalida,IdFuncNaoExiste,ErroInserir,VendaNaoExiste,TipoNaoExiste, JoinVendas
from infraestrutura.to_dict import to_dict, to_dict_list


vendas_app = Blueprint('vendas_app', __name__, template_folder='templates')

@vendas_app.route('/cadastroVendas', methods=['GET'])
@login_required
def login():
   return render_template("CadastroVendas.html")

@vendas_app.route('/vendas', methods=['GET'])
@login_required
def listar():
    listar = Vendas.get(Vendas)
    return jsonify (listar)

@vendas_app.route('/vendas/<int:id>', methods=['GET'])
@login_required
def localizar(id):
    try:
        return jsonify(to_dict(Venda.get(Venda,id))), 200
    except VendaNaoExiste:
        return 'menssagem: Venda não foi encontrada.', 404


@vendas_app.route('/vendas', methods=['POST'])
@login_required
def criar():
    dataVenda = request.form["dataVenda"]
    contrato = request.form["nContrato"]
    tipoContrato = request.form["iTipoContrato"]
    tipoPagamento = request.form["cTipoPagamento"]
    funcionario = request.form["nMatricula"]
    cliente = request.form["nCpf"]

    dadosVendas = {
        "dataVenda": dataVenda,
        "nContrato": contrato,
        "iTipoContrato": tipoContrato,
        "cTipoPagamento": tipoPagamento,
        "nMatricula": funcionario,
        "nCpf":cliente
    }

    try:
        criaVenda = Vendas.post(Vendas, cliente,funcionario)

        return render_template('Venda_Sucesso.html')
        
    except IdJaExiste:
        return  "mensagem:ID venda já existe.", 500
    except IdFuncNaoExiste:
        return "mensagem: Funcionario não encontrado", 404
    except IdClienteNaoExiste:
        return "mensagem: Cliente não encontrado.", 404
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir a venda, verifique a integridade.", 500
    except DataInvalida:
        return "mensagem: Data invalida.", 500
    except TipoNaoExiste:
        return "mensagem: Tipo venda não encontrado", 404

@vendas_app.route('/vendas/<int:id>', methods=['PUT'])
@login_required
def atualizar(id):
    try:
        atualizado = Venda.put(Venda,id)
        return jsonify(to_dict(atualizado)), 201
    except IdFuncNaoExiste:
        return "mensagem: Funcionario não encontrado", 404
    except IdClienteNaoExiste:
        return "mensagem: Cliente não encontrado.", 404
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir a venda, verifique a integridade.", 500
    except DataInvalida:
        return "mensagem: Data invalida.", 500
    except TipoNaoExiste:
        return "mensagem: Tipo venda não encontrado", 404


@vendas_app.route('/vendas/<int:id>', methods=['DELETE'])
@login_required
def remover(id):
    try:
        removido = Venda.delete(Venda,id)
        return jsonify(to_dict(removido))
    except VendaNaoExiste:
        return 'menssagem: Venda não encontrada.'

@vendas_app.route('/getJoin', methods=['GET'])
def getJoin():
    return jsonify(JoinVendas.getJoin())  

@vendas_app.route('/getVendas', methods=['GET'])
def getVendas():
    return render_template("getVendas.html")      
 