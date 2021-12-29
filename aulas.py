n1 = float(input('\033[1;31mDigite aqui a primeira nota:\033[m '))
n2 = float(input('\033[1;32mDigite aqui a segunda nota:\033[m '))
n3 = float(input('\033[1;33mDigite aqui a terceita nota:\033[m '))
n4 = float(input('\033[1;34mDigite aqui a quarta nota:\033[m '))
m = (n1 + n2 + n3 + n4)/4
print(f'Sua média é {m:.2f}')
if m >= 6:
    print('Parabéns! Você passou!')
else:
    print("Seu burro! Vai ter que fazer de novo!")