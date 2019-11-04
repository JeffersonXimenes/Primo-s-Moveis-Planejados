from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required
from resources.feedback import Feedbacks, IdJaExiste,VendaNaoExiste,ErroInserir,NaoExiste
from infraestrutura.to_dict import to_dict, to_dict_list


feedback_app = Blueprint('feedback_app', __name__, template_folder='templates')

@feedback_app.route('/cadastrofeedback', methods=['GET'])
@login_required
def login():
   return render_template("Avaliar_Feedback.html")

@feedback_app.route('/feedback', methods=['GET'])
@login_required
def listar():
    listar = Feedbacks.get(Feedbacks)
    return jsonify (listar)

@feedback_app.route('/feedback/<int:id>', methods=['GET'])
@login_required
def localizar(id):
    try:
        return jsonify(to_dict(Feedbacks.getID(Feedbacks,id))), 200
    except NaoExiste:
        return 'menssagem: Feedback não foi encontrado.', 404


"""

@feedback_app.route('/feedback', methods=['POST'])
@login_required
def criar():
    dataVenda = request.form["dataVenda"]
    contrato = request.form["nContrato"]
    tipoContrato = request.form["iTipoContrato"]
    tipoPagamento = request.form["cTipoPagamento"] 
    funcionario = request.form["cFuncionario"] 
    cliente = request.form["cCliente"] 

    dadosFeed = {
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

"""