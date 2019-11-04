from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required
from resources.feedback import Feedbacks, IdJaExiste,VendaNaoExiste,ErroInserir,NaoExiste
from infraestrutura.to_dict import to_dict, to_dict_list


feedback_app = Blueprint('feedback_app', __name__, template_folder='templates')


@feedback_app.route('/cadastrofeedback', methods=['GET'])
#@login_required
def login():
   return render_template("Avaliar_Feedback.html")

@feedback_app.route('/feedback', methods=['GET'])
#@login_required
def listar():
    listar = Feedbacks.get(Feedbacks)
    return jsonify (listar)

@feedback_app.route('/feedback/<int:id>', methods=['GET'])
#@login_required
def localizar(id):
    try:
        return jsonify(Feedbacks.getID(Feedbacks,id)), 200
    except NaoExiste:
        return 'menssagem: Feedback não foi encontrado.', 404



@feedback_app.route('/feedback', methods=['POST'])
#@login_required
def criar():
    
    '''ambiente = request.form["ambiente"]
    notaAtendimento = request.form["notaAtendimento"]
    notaVendedor = request.form["notaVendedor"]
    notaMontagem = request.form["notaMontagem"]
    mensagem = request.form["mensagem"]
    pedido = request.form["cPedido"]

    dadosFeed = {
        'ambiente': ambiente,
        'notaAtendimento': notaAtendimento,
        'notaVendedor': notaVendedor,
        'notaMontagem': notaMontagem,
        'mensagem': mensagem,
        'cPedido': pedido
    }'''

    try:
        criado = Feedbacks.post(Feedbacks)
        return 'Feed criado com sucesso ! ', 201
    except IdJaExiste:
        return  "mensagem:ID feed já existe.", 500
    except VendaNaoExiste:
        return "mensagem: Venda não encontrada", 404
    except ErroInserir:
        return "mensagem: Erro ao inserir ! ", 404

