
print('='*60)

salario = float(input('{}Digite o salario liquido: '.format(' '*4)))
#mostrando o salario liquido e sua distribuição
print('{}O salario liquido é:{}R${:7.2f}'. format(' '*4, ' '*7 ,salario))
print('{}Gastos E:{}R${:7.2f}'. format(' '*4, ' '*18, salario*0.5))
print('{}Investimentos LP:{}R${:7.2f}'. format(' '*4, ' '*10, salario*0.2))
print('{}Investimentos CP:{}R${:7.2f}'. format(' '*4, ' '*10, salario*0.1))
print('{}Livre:{}R${:7.2f}'. format(' '*4, ' '*21, salario*0.2))
print('='*60)