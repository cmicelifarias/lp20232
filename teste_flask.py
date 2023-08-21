from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Ola</h1>"

@app.route("/buda")
def hellodenovo():
    return "<h1>Sou outra pagina</h1>"

app.run()

