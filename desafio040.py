n1 = float(input('Digite aqui a sua primeira nota: '))
n2 = float(input('Digite aqui a sua segunda nota: '))
n3 = float(input('Digite aqui a sua terceira nota: '))
n4 = float(input('Digite aqui a sua quarta nota: '))
m = (n1 + n2 + n3 + n4)/4
if m >= 7:
    print(f'Sua média é {m} e você foi APROVADO!')
elif m < 5:
    print(f'Sua média é {m} e você foi REPROVADO!')
else:
    print(f'Sua média é {m} e você está de RECUPERAÇÃO!')
