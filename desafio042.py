r1 = float(input('Digite aqui o valor da primeira reta: '))
r2 = float(input('Digite aqui o valor da segunda reta: '))
r3 = float(input('Digite aqui o valor da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('É possível formar um triângulo com essas retas!')
    if r1 == r2 == r3:
        print('Esse triângulo é EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse triângulo é ISÓSCELES')
    else:
        print('Esse triângulo é ESCALENO')
else:
    print('Não é possível formar um triângulo com essas retas...')
