from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.cliente import Clientes,Cliente
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

#api.add_resource(Clientes, '/clientes')
#api.add_resource(Cliente, '/clientes/<string:cCliente>')

@app.route('/clientes')
def clientes():
    return render_template('/clientes.html')


if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)