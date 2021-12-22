n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1+n2
mult = n1*n2
div = n1/n2
sub = n1-n2
pot = n1**n2
print('A soma {} e {} vale {}, o produto vale {}, a subtração é {}, a divisão é {:.3f}'.format(n1, n2, soma, mult, sub, div))
print('{} elevado a {} é {}'.format(n1, n2, pot))