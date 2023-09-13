from flask import Flask, render_template, redirect, request, flash, send_from_directory
import json
import random
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LALA'

@app.route('/')
def page1():
    return render_template('calculo.html')

@app.route('/calculoTop', methods=['POST'])
def calculoTop():
    altura = int(request.form.get('altura'))
    idade = int(request.form.get('idade'))
    atividade = float(request.form.get('atividade'))
    peso = int(request.form.get('peso'))
    sexo = int(request.form.get('sexo'))
    objetivo = int(request.form.get('objetivo'))
    velocidade = int(request.form.get('velocidade'))

    if objetivo == 1:
        pesoAlcancar = 0
    else:
        pesoAlcancar = int(request.form.get('pesoAlcancar'))


    if sexo == 1:
        tmb = (88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)) * atividade
    else:
        tmb = (447.593  + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)) * atividade
    
    if objetivo == 1:
        kcalPDia = math.ceil(tmb)
        tempo = 0
    elif objetivo == 2:
        necessario = (pesoAlcancar - peso) * 7000
        tempo = necessario / velocidade
        kcalPDia = math.ceil((velocidade / 7) + tmb)
    elif objetivo == 3:
        necessario = (peso - pesoAlcancar) * 7000
        tempo = necessario / velocidade
        kcalPDia = math.ceil(tmb - (velocidade / 7))
    
    info = [
        {
            'kcalNecessarias': kcalPDia,
            'tempo': tempo
        }
    ]
    with open('./JSON/inputValue.json', 'w') as gravarTemp:
        json.dump(info, gravarTemp, indent=4)
    return redirect('/gerarTodos')

@app.route('/gerarTodos')
def gerarTodos():
    with open('./JSON/inputValue.json', 'r') as valueTemp:
        values = json.load(valueTemp)
    for i in values:
        qtdCalorias = i.get('kcalNecessarias')
    qtdCafe = 0.2 * qtdCalorias
    with open('./JSON/alimentos.json', 'r', encoding='utf-8') as comidasTemp:
        comidas = json.load(comidasTemp)
    descricoes_unicas = set()
    comidas_sem_duplicatas = []
    for i in comidas:
        descricao = i.get('descricao')
        separar = i.get('calorias')
        calorias = int(separar.split()[0])

        if descricao not in descricoes_unicas and calorias <= qtdCafe:
                descricoes_unicas.add(descricao)
                comidas_sem_duplicatas.append(i)
    ramdomic = random.sample(comidas_sem_duplicatas, 3)
    cardapioNovo = []
    cardapioNovo = ramdomic    
    with open('./JSON/cafeDaManhaDieta.json', 'w', encoding='utf-8') as gravarTemp:
        json.dump(cardapioNovo, gravarTemp, indent=4)
    return redirect('/page2')

@app.route('/page2')
def dieta():
    with open('./JSON/cafeDaManhaDieta.json', 'r', encoding='utf-8') as Temp:
        comida = json.load(Temp)
    with open('./JSON/inputValue.json', 'r') as valueTemp:
        values = json.load(valueTemp)
    for i in values:
        calorias = i.get('kcalNecessarias')
        tempo = i.get('tempo')
    return render_template('dieta.html', comidas = comida, calorias = calorias, tempo = tempo)

@app.route('/salvar')
def salvar():
    with open('./JSON/cafeDaManhaDieta.json', 'r', encoding='utf-8') as Temp:
        cafe = json.load(Temp)
    with open('./JSON/inputValue.json', 'r', encoding='utf-8') as inputTemp:
        inputvalue = json.load(inputTemp)

    with open('./JSON/Salvo/cafeDaManhaDietaSalvo.json', 'w', encoding='utf-8') as GravarCafeSalvo:
        json.dump(cafe, GravarCafeSalvo, indent=4)
    with open('./JSON/Salvo/inputValueSalvo.json', 'w', encoding='utf-8') as GravarInputSalvo:
        json.dump(inputvalue, GravarInputSalvo, indent=4)

    return redirect('/DietaSalva')

@app.route('/DietaSalva')
def DietaSalva():
    with open('./JSON/Salvo/cafeDaManhaDietaSalvo.json', 'r', encoding='utf-8') as CafeTemp:
        cafeSalvo = json.load(CafeTemp)
    with open('./JSON/Salvo/inputValueSalvo.json', 'r', encoding='utf-8') as inputSalvoTemp:
        inputvalueSalvo = json.load(inputSalvoTemp)

    for i in inputvalueSalvo:
        calorias = i.get('kcalNecessarias')
        tempo = i.get('tempo')

    return render_template("salvo.html", comidas = cafeSalvo, calorias = calorias, tempo = tempo)

@app.route('/gerarCafe')
def gerarCafe():
    with open('./JSON/inputValue.json', 'r') as valueTemp:
        values = json.load(valueTemp)
    for i in values:
        qtdCalorias = i.get('kcalNecessarias')
    qtdCafe = 0.2 * qtdCalorias
    with open('./JSON/alimentos.json', 'r', encoding='utf-8') as comidasTemp:
        comidas = json.load(comidasTemp)
    descricoes_unicas = set()
    comidas_sem_duplicatas = []
    for i in comidas:
        descricao = i.get('descricao')
        separar = i.get('calorias')
        calorias = int(separar.split()[0])

        if descricao not in descricoes_unicas and calorias <= qtdCafe:
                descricoes_unicas.add(descricao)
                comidas_sem_duplicatas.append(i)
    ramdomic = random.sample(comidas_sem_duplicatas, 3)
    cardapioNovo = []
    cardapioNovo = ramdomic    
    with open('./JSON/cafeDaManhaDieta.json', 'w', encoding='utf-8') as gravarTemp:
        json.dump(cardapioNovo, gravarTemp, indent=4)
    return redirect('/page2')

if __name__ in "__main__":
    app.run(debug=True)