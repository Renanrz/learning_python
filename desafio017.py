import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = (math.sqrt(co**2+ca**2))
print(f'A hipotenusa do seu triangulo é {h:.2f}')
