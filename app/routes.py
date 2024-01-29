from app import app
from flask import render_template, request

@app.route('/', defaults={"nome":"Usuário"})
@app.route('/index', defaults={"nome":"Usuário"})
@app.route('/index/<nome>')
def index(nome):
    dados = {"profissao" : "Servidor Público", "orgao": "SES GO" }

    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login')
def login():
    return render_template('login.html')    

@app.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')

    return "usuario: {} e senha: {}".format(usuario, senha)