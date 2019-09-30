print('='*60)

frase = input('Digite uma frase: ')
letra = input('Digite uma letra: ')

print('{0}A letra foi encontrada {1} vezes'.format(' '*4, frase.count(letra)))
print('{0}A letra foi encontrada pela primeira vez na posição {1}'.format(' '*4,frase.index(letra)))
print('{0}A letra foi encontrada pela ultima vez na posição {1}'.format(' '*4,frase.rindex(letra)))

print('='*60)