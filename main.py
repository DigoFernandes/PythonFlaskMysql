
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

config = {"user": "root", "password": "", "host": "localhost", "database": "liza"}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()


if conn.is_connected():
    print("Conexão bem-sucedida ao banco de dados.")


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login_validation", methods=["POST"])
def login_validation():
    email = request.form.get("email")
    senha = request.form.get("senha")

    cursor.execute(
        "SELECT * FROM `usuarios` WHERE `email` = %s AND `senha` = %s", (email, senha)
    )
    usuarios = cursor.fetchall()
    if len(usuarios) > 0:
        return render_template("home.html")

    return render_template("login.html")



@app.route("/add_usuario", methods=["POST"])
def add_user():
    
    nomeR = request.form.get("emailRegistro")
    senhaR = request.form.get("senhaRegistro")
    
    cursor.execute(
        "INSERT INTO `usuarios` (`email`, `senha`) VALUES (%s, %s)", (nomeR, senhaR)
    )
    conn.commit()
    return "Deu certo"
if __name__ == "__main__":
    app.run(debug=True)
