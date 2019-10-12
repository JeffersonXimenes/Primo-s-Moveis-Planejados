from flask import Blueprint, jsonify, request, render_template
from resources.venda import Venda,Vendas,IdJaExiste,IdClienteNaoExiste,\
    DataInvalida,IdFuncNaoExiste,ErroInserir,VendaNaoExiste,TipoNaoExiste
from infraestrutura.to_dict import to_dict, to_dict_list


vendas_app = Blueprint('vendas_app', __name__, template_folder='templates')

@vendas_app.route('/cadastroVendas', methods=['GET'])
def login():
   return render_template("CadastroVendas.html")

@vendas_app.route('/vendas', methods=['GET'])
def listar():
    listar = Vendas.get(Vendas)
    return jsonify (listar)

@vendas_app.route('/vendas/<int:id>', methods=['GET'])
def localizar(id):
    try:
        return jsonify(to_dict(Venda.get(Venda,id))), 200
    except VendaNaoExiste:
        return 'menssagem: Venda não foi encontrada.', 404


@vendas_app.route('/vendas', methods=['POST'])
def criar():
    dataVenda = request.form["dataVenda"]
    contrato = request.form["nContrato"]
    tipoContrato = request.form["iTipoContrato"]
    tipoPagamento = request.form["cTipoPagamento"] 
    funcionario = request.form["cFuncionario"] 
    cliente = request.form["cCliente"] 

    dadosVendas = {
        "dataVenda": dataVenda,
        "nContrato": contrato,
        "iTipoContrato": tipoContrato,
        "cTipoPagamento": tipoPagamento,
        "cFuncionario": funcionario,  
        "cCliente":cliente  
    }

    try:
        criaVenda = Vendas.post(Vendas, dadosVendas)

        return 'Venda criado com sucesso ! ', 201
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
def remover(id):
    try:
        removido = Venda.delete(Venda,id)
        return jsonify(to_dict(removido))
    except VendaNaoExiste:
        return 'menssagem: Venda não encontrada.'


