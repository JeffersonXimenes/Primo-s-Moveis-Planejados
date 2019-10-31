from infraestrutura.sql_alchemy import banco
from app import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(banco.Model, UserMixin):
    __tablename__ = 'users'
    id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String(86), nullable=False)
    email = banco.Column(banco.String(84), nullable=False, unique=True)
    password = banco.Column(banco.String(128), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
