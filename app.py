from flask import Flask, jsonify
from flask_restful import Api
from clientes_api import clientes_app
from telefones_api import telefones_app
from enderecos_api import enderecos_app
from cargos_api import cargo_app
from funcionarios_api import funcionarios_app
from tipoPagamento_api import tipoPagamento_app
from vendas_api import vendas_app


app = Flask(__name__)
app.register_blueprint(clientes_app)
app.register_blueprint(telefones_app)
app.register_blueprint(enderecos_app)
app.register_blueprint(cargo_app)
app.register_blueprint(funcionarios_app)
app.register_blueprint(tipoPagamento_app)
app.register_blueprint(vendas_app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

@app.route('/')
def all():
    from models.clientes import ClienteModel
    from models.telefone_models import TelefoneModel
    from models.endereco_models import EnderecoModel
    from models.cargo_models import CargoModel
    from models.funcionario_models import FuncionarioModel
    from models.tipoPagamento_models import TipoPagamentoModel
    from models.vendas_models import VendasModel
    database = [{'clientes': [cliente.json() for cliente in ClienteModel.query.all()],
                'telefones': [telefone.json() for telefone in TelefoneModel.query.all()],
                'endereços': [endereco.json() for endereco in EnderecoModel.query.all()],
                'cargos': [cargo.json() for cargo in CargoModel.query.all()],
                'funcionarios': [funcionario.json() for funcionario in FuncionarioModel.query.all()],
                'tipo_pagamento': [pagamento.json() for pagamento in TipoPagamentoModel.query.all()],
                'vendas': [venda.json() for venda in VendasModel.query.all()]}]
    return jsonify(database)


#api.add_resource(Clientes, '/clientes')
#api.add_resource(Cliente, '/clientes/<int:cCliente>')
#api.add_resource(Telefones, '/telefones')
#api.add_resource(Telefone, '/telefones/<int:cTelefone>')

if __name__ == '__main__':
    from infraestrutura.sql_alchemy import banco
    banco.init_app(app)
    app.run(host='localhost', port=5000)
