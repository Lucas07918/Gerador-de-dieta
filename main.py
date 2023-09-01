from flask import Flask, render_template, redirect, request, flash, send_from_directory
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LALA'

@app.route('/')
def page1():
    with open('./JSON/alimentos.json', 'r', encoding='utf-8') as Temp:
        comida = json.load(Temp)
    return render_template('dieta.html', comidas = comida)

@app.route('/page2', methods=['POST'])
def page2():
    with open('./JSON/alimentos.json', 'r', encoding='utf-8') as Temp:
        comida = json.load(Temp)
    return render_template('dieta.html', comidas = comida)

if __name__ in "__main__":
    app.run(debug=True)