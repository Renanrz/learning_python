vp = float(input('Digite aqui o valor do produto em R$: '))
print('''[1] À vista no dinheiro ou cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] Em 3x ou mais no cartão''')
op = int(input('Digite aqui a opção desejada: '))
if op == 1:
    print(f'O valor do produto terá 10% de desconto e custará R${vp * 0.9:.2f}')
elif op == 2:
    print(f'O valor do produto terá 5% de desconto e custará R${vp * 0.95:.2f}')
elif op == 3:
    print(f'O valor do produto não terá desconto e custará R${vp:.2f}')
elif op == 4:
    print(f'O valor do produto terá 20% de juros e custará R${vp * 1.2:.2f}')
else:
    print('A opção digitada é inválida. Favor tentar novamente')