from flask import Blueprint, jsonify, request, render_template
from resources.acompanhamentoPedido import AcompanhamentoPedido,AcompanhamentoNaoExiste, IdFuncNaoExiste, IdVendaNaoExiste,\
    DataInvalida,ErroInserir
from infraestrutura.to_dict import to_dict, to_dict_list
from flask_login import login_required

acompanhamento_app = Blueprint('acompanhamento_app', __name__, template_folder='templates')

@acompanhamento_app.route('/acompanhamentoPedido', methods=['GET'])
@login_required
def login():
   return render_template("DiarioDeBordo.html")

@acompanhamento_app.route('/cadastroAcompanhamento', methods=['GET'])
@login_required
def listar():
    listar = AcompanhamentoPedido.get(AcompanhamentoPedido)
    return jsonify(listar)
 

@acompanhamento_app.route('/cadastroAcompanhamento', methods=['POST'])
@login_required
def criar():
    descricao = request.form["iDescricao"]  
    dataAtualizacao = request.form["dataAtualizacao"]
    matricula = request.form["cFuncionario"]
    pedido = request.form["cPedido"]
    
    dados = {"iDescricao": descricao, "cFuncionario": matricula, "cPedido": pedido,"dataAtualizacao": dataAtualizacao}

    try:
        AcompanhamentoPedido.post(AcompanhamentoPedido, matricula)
        return 'Acompanhamento cadastrado com sucesso', 201
    
    except IdVendaNaoExiste:
        return "mensagem: Pedido não encontrado.", 500
    except IdFuncNaoExiste:
        return "mensagem: Funcionario não encontrado.", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o endereco.", 500
    except DataInvalida:
        return "mensagem: Data invalida.", 500

