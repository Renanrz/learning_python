wages = float(input('Digite aqui o seu salário: '))
if wages > 1250:
    print(f'Seu salário reajustado será de {(wages * 1.1):.2f}')
else:
    print(f'Seu salário reajustado será de {(wages * 1.15):.2f}')