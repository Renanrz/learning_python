import random

print('PEDRA - PAPEL - TESOURA')
p1 = str(input('Selecione entre Pedra, Papel e Tesoura: ')).lower().strip()
list = ['pedra', 'papel', 'tesoura']
p2 = random.choice(list)
if p1 == 'pedra' and p2 == 'tesoura':
    print(f'Você escolheu {p1} e o computador escolheu {p2}. Você \033[;32mGANHOU!\033[m')
elif p1 == 'tesoura' and p2 == 'papel':
    print(f'Você escolheu {p1} e o computador escolheu {p2}. Você \033[;32mGANHOU!\033[m')
elif p1 == 'papel' and p2 == 'pedra':
    print(f'Você escolheu {p1} e o computador escolheu {p2}. Você \033[;32mGANHOU!\033[m')
elif p2 == 'pedra' and p1 == 'tesoura':
    print(f'Você escolheu {p1} e o computador escolheu {p2}. Você \033[;31mperdeu!\033[m')
elif p2 == 'tesoura' and p1 == 'papel':
    print(f'Você escolheu {p1} e o computador escolheu {p2}. Você \033[;31mperdeu!\033[m')
elif p2 == 'papel' and p1 == 'pedra':
    print(f'Você escolheu {p1} e o computador escolheu {p2}. Você \033[;31mperdeu!\033[m')
elif p1 == p2:
    print(f'Você e o computador escolheram {p2}. O jogou \033[;33mempatou...\033[m')
else:
    print('Burro! Você sabe jogar essa merda? Escolhe uma das três opções aí o carai...')