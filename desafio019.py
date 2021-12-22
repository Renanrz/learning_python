import random

a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
num = random.randint(1, 4)
if num == 1:
    print(a1)
if num == 2:
    print(a2)
if num == 3:
    print(a3)
if num == 4:
    print(a4)
