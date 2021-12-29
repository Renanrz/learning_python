year = float(input('Digite aqui um ano: '))
if year % 4 == 0:
    print(f'O ano de {abs(year)} é bissexto!')
else:
    print(f'O ano de {abs(year)} não é bissexto...')
