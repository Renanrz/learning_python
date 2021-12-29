d = int(input('Qual a distancia da viagem em km? '))
dc = d/2
dl = d * 0.45
if d <= 200:
    print(f'O preço da passagem é de R${abs(dc):.2f}')
else:
    print(f'O preço da passagem é de R${dl:.2f}')