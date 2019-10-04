from flask import Flask , render_template , redirect, request
from investimen import Investimento 
from ctinvest import Carteira_investimento



investiment1 = Investimento('Renda Fixa','Tesouro Direto',1000.00 , 0.1,'mês', )
lista = [investiment1]

app=Flask(__name__)

@app.route('/') 
def home():
    return render_template('home.html', lista = lista)





app.run()