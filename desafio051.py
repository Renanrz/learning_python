print('''================================
    10 TERMOS DE UMA PA
================================''')
n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão: '))
n3 = int(input('Quantos termos você deseja que seja mostrado: '))
d = n1 + (n3 - 1) * n2
for c in range(n1, d, n2):
    print(c, end=' -> ')
print('END')