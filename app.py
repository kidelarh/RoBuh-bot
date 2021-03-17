from flask import Flask, render_template, request
from db import perguntas,respostas,fallback,disparidades,respostasd
import numpy as np

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")

def get_bot_response():
    userText = request.args.get('msg')
    for i in [i for i,x in enumerate(perguntas) if x != userText]:
       res = fallback

    for i in [i for i,x in enumerate(perguntas) if x == userText]:
       res = respostas[i]

    for i in [i for i,x in enumerate(disparidades) if x == userText]:
       res = respostasd[i]

    return str(res)

if __name__ == "__main__":
    app.run() 
