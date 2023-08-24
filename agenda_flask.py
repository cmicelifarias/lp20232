from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def hello_agendeca():
    return render_template("principal.html")

@app.route("/", methods = ["POST"])
def login():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
    if nome == "Buda" and senha=="Buda":
        return "Vemos na proxima aula"
    else:
        return "<h1>Errou</h1>"



app.run()
