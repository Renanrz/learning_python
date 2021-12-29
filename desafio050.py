print('O PROGRAMA TE PEDIRÁ 6 NÚMEROS INTEIROS. DIGITE UM A UM')
s = 0
for c in range(0, 6):
    n = int(input('Digite aqui um número inteiro: '))
    if n % 2 == 0:
        s = s + n
print(f'A soma dos valores pares dos números escolhidos é {s}')
