v = float(input('Digite aqui a velocidade do seu carro em km/h: '))
fine = (v - 80) * 7
if v > 80:
    print(f'Seu carro foi multado! A sua multa é de R${fine:.2f}')
