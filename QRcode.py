from flask import Flask, render_template, request
import sqlite3
import qrcode

QRcode = Flask(__name__)

@QRcode.route("/")
def pagina_inicial():
    return render_template("index.html")

@QRcode.route("/login", methods = ["POST"])
def login():

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        return Buscar_usuario(usuario,senha) 
    
    else:
        print("ERRO")
        return "ERRO"

def Buscar_usuario(usuario,senha):

    # obs: criar um banco de dados decente depois.

    arquivo = open("./senha.txt","r+")

    linha = arquivo.readlines()

    teste = usuario+"-"+senha+"\n"

    if teste in linha:
        return render_template("inserir_infos.html")
    else:
        return render_template("index.html", erro="Login Incorreto")
    
    print(linha)

'''@QRcode.route("/info", methods = ["POST"])
def gerar_Qrcode():
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    site = request.form["site"]
    email = request.form["email"]
    imagem = qrcode.make(f'{nome},{telefone},{site},{email}')
    imagem.save(f"qr {nome}.png")

    return render_template("Qrcode.html", Qr= f"qr {nome}.jpg")'''

QRcode.run()
