from flask import Flask, render_template, request, redirect
from Alunos import Alunos

pagina_nome = 'Lista Alunos'
aluno1 = Alunos('Lucas', 'Calminho', 47999705773)
aluno2 = Alunos('Lais', 'Hoffmann', 679991720831)
aluno3 = Alunos('Leonardo', 'Silva', 47984115831)
aluno4 = Alunos('Guto', 'Carioca', 49992036808)
aluno5 = Alunos('Guilherme', 'Krammer', 47997221306)
aluno6 = Alunos('Tito','Deluchi', 47997534229)
aluno7 = Alunos('Lucas', 'Brabinho', 47992098467)
aluno8 = Alunos('Lucas', 'Pedroso', 47997007558)
aluno9 = Alunos('Josiane', 'Sardá', 47988640334)
lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5 , aluno6, aluno7, aluno8, aluno9]

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', nome = pagina_nome , lista = lista_alunos)

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    telefone = request.form['telefone']    
    aluno_novo = Alunos(nome, sobrenome, telefone)
    lista_alunos.append(aluno_novo)
    return redirect('/')    

app.run()
