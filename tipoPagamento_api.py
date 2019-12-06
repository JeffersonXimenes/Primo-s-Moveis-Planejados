from flask import Blueprint, jsonify, request
from flask_login import login_required
from resources.tipo_pagamento import TipoPagamento,TipoPagamentos,IdJaExiste,ErroInserir,TipoNaoExiste
from infraestrutura.to_dict import to_dict, to_dict_list


tipoPagamento_app = Blueprint('tipoPagamento_app', __name__, template_folder='templates')


@tipoPagamento_app.route('/tipoPagamento', methods=['GET'])
#@login_required
def listar():
    listar = TipoPagamentos.get(TipoPagamentos)
    return jsonify (listar)

@tipoPagamento_app.route('/tipoPagamento/<int:id>', methods=['GET'])
#@login_required
def localizar(id):
    try:
        return jsonify(to_dict(TipoPagamento.get(TipoPagamento,id))), 200
    except TipoNaoExiste:
        return 'menssagem: Tipo de pagamento não foi encontrado.', 404

@tipoPagamento_app.route('/tipoPagamento', methods=['POST'])
#@login_required
def criar():
    try:
        criado = TipoPagamentos.post(TipoPagamentos)
        return jsonify (to_dict(criado)), 201
    except IdJaExiste:
        return  "mensagem:Id do tipo de pagamento já existe", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o tipo de pagamento.", 500

@tipoPagamento_app.route('/tipoPagamento/<int:id>', methods=['PUT'])
#@login_required
def atualizar(id):
    try:
        atualizado = TipoPagamento.put(TipoPagamento,id)
        return jsonify(to_dict(atualizado)), 201
    except IdJaExiste:
        return "mensagem:Id do cargo já existe", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o cargo.", 500

@tipoPagamento_app.route('/tipoPagamento/<int:id>', methods=['DELETE'])
#@login_required
def remover(id):
    try:
        removido = TipoPagamento.delete(TipoPagamento,id)
        return jsonify(removido)
    except TipoNaoExiste:
        return 'menssagem: Tipo de pagamento não encontrado.'


