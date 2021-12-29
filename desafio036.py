vc = float(input('Digite aqui o valor da casa: '))
sal = float(input('Digite aqui o seu salario em R$: '))
pa = int(input('Digite aqui em quantos anos você quer pagar essa casa: '))
vpm = vc/(pa * 12)
if vpm > 0.3 * sal:
    print('O seu empréstimo foi negado devido ao valor da prestação representar mais do que 30% do seu salário')
else:
    print(f'O valor da sua prestação é de R${vpm:.2f}')