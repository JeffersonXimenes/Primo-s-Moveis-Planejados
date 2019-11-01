from flask import render_template, request, redirect, url_for,jsonify
from flask_login import login_user, logout_user
from app import app
from models.user_models import User


@app.before_first_request
def cria_banco():
    banco.create_all()

@app.route('/')
def home():
    return render_template('CadastroClientes.html')

@app.route('/paginainicial')
def paginainicial():
    return render_template('index.html')

#apaga eu dps
@app.route('/feedback')
def feedback():
    return render_template('Avaliar_Feedback.html')

# também posso ser apagado heiiin gatinho <3

@app.route('/agendarSuporte')
def agendarSuporte():
    return render_template('Agendar_Suporte.html')

# campo acima deve ser apagado    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']

        user = User(name, email, pwd)
        banco.session.add(user)
        banco.session.commit()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))        

        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    from infraestrutura.sql_alchemy import banco
    banco.init_app(app)
    app.run(host='localhost', port=5000)