import random
print('O computador escolheu um numero inteiro entre 0 e 5...')
np = int(input('Qual número você acha que o computador escolheu? '))
nc = random.randint(0, 5)
if np == nc:
    print(f'Você acertou! O número escolhido pelo computador foi {np}')
else:
    print(f'Você errou... O número escolhido pelo computador foi {nc}')