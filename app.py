from flask import Flask, jsonify
from flask_restful import Api
from resources.cliente import Clientes,Cliente
from resources.telefone import Telefones,Telefone
from clientes_api import clientes_app
from telefones_api import telefones_app


app = Flask(__name__)
app.register_blueprint(clientes_app)
app.register_blueprint(telefones_app)
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
    database = {'clientes': [cliente.json() for cliente in ClienteModel.query.all()],
                'telefones': [telefone.json() for telefone in TelefoneModel.query.all()]}
    return jsonify(database)


#api.add_resource(Clientes, '/clientes')
#api.add_resource(Cliente, '/clientes/<int:cCliente>')
#api.add_resource(Telefones, '/telefones')
#api.add_resource(Telefone, '/telefones/<int:cTelefone>')

if __name__ == '__main__':
    from infraestrutura.sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
