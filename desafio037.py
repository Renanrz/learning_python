import math
n = int(input('Digite um numero inteiro: '))
method = int(input('1 - Binário\n'
                   '2 - Octal\n'
                   '3 - Hexadecimal\nSelecione o número associado à base de conversão: '))
if method == 1:
    print(f'O número {n} convertido para sua forma binária é {bin(n)[2:]}')
elif method == 2:
    print(f'O número {n} convertido para a sua forma octal é {oct(n)[2:]}')
elif method == 3:
    print(f'O número {n} convertido para a sua forma hexadecimal é {hex(n)[2:]}')
else:
    print('Você não escolheu nenhum método valido. \nPor favor, volte ao início e escolha entre as opcões 1, 2 e 3')
