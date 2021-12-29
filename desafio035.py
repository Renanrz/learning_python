r1 = float(input('Digite aqui o valor da primeira reta: '))
r2 = float(input('Digite aqui o valor da segunda reta: '))
r3 = float(input('Digite aqui o valor da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('É possível formar um triângulo com essas retas!')
else:
    print('Não é possível formar um triângulo com essas retas...')