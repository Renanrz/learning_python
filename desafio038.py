print('Comparador de números')
n1 = float(input('Digite aqui o primeiro número: '))
n2 = float(input('Digite aqui o segundo número: '))
print(f'Os números escolhidos foram {n1} e {n2}')
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Os dois valores são iguais...')