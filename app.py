from flask import Flask, jsonify
from flask_login import LoginManager
from flask_restful import Api
from clientes_api import clientes_app
from telefones_api import telefones_app
from enderecos_api import enderecos_app
from cargos_api import cargo_app
from funcionarios_api import funcionarios_app
from tipoPagamento_api import tipoPagamento_app
from vendas_api import vendas_app
from acompanhamento_api import acompanhamento_app
from feedback_api import feedback_app
from chamado_api import chamados_app


app = Flask(__name__)
app.register_blueprint(acompanhamento_app)
app.register_blueprint(clientes_app)
app.register_blueprint(telefones_app)
app.register_blueprint(enderecos_app)
app.register_blueprint(cargo_app)
app.register_blueprint(funcionarios_app)
app.register_blueprint(tipoPagamento_app)
app.register_blueprint(vendas_app)
app.register_blueprint(feedback_app)
app.register_blueprint(chamados_app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'segredo'
api = Api(app)
login_manager = LoginManager(app)



