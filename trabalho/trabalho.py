from flask import Flask, render_template

class Cerveja:

    def __init__(self, codigo, nome, embalagem , preco):
        self.codigo = codigo
        self.embalagem = embalagem
        self.nome = nome
        self.preco = preco


beer1 = Cerveja('1010', 'Patagônia Amber Lager', '600ml', 4.69)
beer2 = Cerveja('1011','Patagônia Ipa','600ml', 4.69)
beer3 = Cerveja('1012','Patagônia weisse','600ml',4.69)
beer4 = Cerveja('1013','Pilssener','600ml',4.59)
beer5 = Cerveja('2010','Stella Artois','355ml',1.39)
beer6 = Cerveja('3010','Budweiser','355ml', 1.39)
beer7 = Cerveja('4010','Corona','355ml',1.79)
beer8 = Cerveja('5010','Beck´s', '350ml',1.59)
beer9 = Cerveja('6010','Bohemia', '365ml',1.09)
beer10 = Cerveja('7010','Brahma', '365ml',0.99)
beer11= Cerveja('8010','Original', '600ml',1.49)

cervejas_cadastradas = [beer1, beer2, beer3, beer4, beer5, beer6, beer7, beer8, beer9, beer10, beer11]

app=Flask(__name__)


@app.route('/')
def inc():
    return render_template('index.html', titulo_pagina = 'Home')

@app.route('/listar')
def listar():
    return render_template('listar.html' , titulo_pagina = 'listar', lista = cervejas_cadastradas)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo_pagina = 'cadastrar')

@app.route('/pedido')
def pedido():
    return render_template('pedido.html' , titulo_pagina = 'Pedido')    

@app.route('/Salvar', methods =['POST'])
def salvar():
    return 'Salvo'


app.run()