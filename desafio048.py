s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
print(f'A soma de todos os {cont} valores executados é de {s}')