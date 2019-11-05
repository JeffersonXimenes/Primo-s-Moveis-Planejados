from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required
from resources.chamados import Chamados,VendaNaoExiste,IdJaExiste,ErroInserir,\
    DataInvalida,ChamadoNaoExiste


chamados_app = Blueprint('chamados_app', __name__, template_folder='templates')

@chamados_app.route('/agendarSuporte', methods=['GET'])
#@login_required
def login():
   return render_template("Agendar_Suporte.html")

@chamados_app.route('/chamados', methods=['GET'])
#@login_required
def listar():
    listar = Chamados.get(Chamados)
    return jsonify (listar)

@chamados_app.route('/chamados/<int:id>', methods=['GET'])
#@login_required
def localizar(id):
    try:
        return jsonify(Chamados.getID(Chamados,id)), 200
    except ChamadoNaoExiste:
        return 'menssagem: Chamado não foi encontrado.', 404



@chamados_app.route('/chamados', methods=['POST'])
#@login_required
def criar():
    try:
        criar = Chamados.post(Chamados)
        return 'Chamado criado com sucesso ! ', 201
    except IdJaExiste:
        return  "mensagem:ID venda já existe.", 500
    except VendaNaoExiste:
        return "mensagem: Venda não encontrada", 404
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o chamado, verifique a integridade.", 500
    except DataInvalida:
        return "mensagem: Data invalida.", 500
    except ChamadoNaoExiste:
        return "mensagem: Chamado não existe. ", 500



"""

@chamados_app.route('/chamados/<int:id>', methods=['DELETE'])
@login_required
def remover(id):
    try:
        removido = Venda.delete(Venda,id)
        return jsonify(to_dict(removido))
    except VendaNaoExiste:
        return 'menssagem: Venda não encontrada.'


"""