name = str(input('Digite o seu nome completo: ')).strip()
list = name.split()
print(f'Primeiro nome: {list[0]}')
print(f'Último nome: {list[-1]}')