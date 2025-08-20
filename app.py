
from flask import Flask, render_template
import os

app = Flask(__name__)

times = ['Sao_Paulo', 'Palmeiras', 'Corinthians', 'Flamengo']
categorias = ['Masculina', 'Feminina', 'Infantil', 'Jogador']
modelos = ['Modelo1', 'Modelo2']

@app.route("/")
def index():
    return render_template("index.html", times=times)

@app.route("/categorias/<time>")
def show_categorias(time):
    return render_template("categorias.html", time=time, categorias=categorias)

@app.route("/modelos/<time>/<categoria>")
def show_modelos(time, categoria):
    return render_template("modelos.html", time=time, categoria=categoria, modelos=modelos)

@app.route('/modelo/<time>/<categoria>/<modelo>')
def show_modelo(time, categoria, modelo):
    caminho = os.path.join('static', 'Camisas', 'img', time, categoria, modelo)
    imagens = [f for f in os.listdir(caminho) if f.endswith('.jpg')]
    return render_template('modelo.html', time=time, categoria=categoria, modelo=modelo, imagens=imagens)
    
if __name__ == "__main__":
    app.run(debug=True)


