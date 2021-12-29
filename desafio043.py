weight = float(input('Digite aqui o seu peso: '))
height = float(input('Digite aqui a sua altura em m: '))
imc = weight / height**2
if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} e você está abaixo do seu peso ideal')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é de {imc:.2f} e você está no seu peso ideal')
elif 25 <= imc < 30:
    print(f'Seu IMC é de {imc:.2f} e você está em SOBREPESO')
elif 30 <= imc < 40:
    print(f'Seu IMC é de {imc:.2f} e você está OBESO')
else:
    print(f'Seu IMC é de {imc:.2f} e seu status é de OBESIDADE MÓRBIDA')
print('''Tabela de IMC:
Abaixo de 18.5 - Abaixo do peso
Entre 18.5 e 25 - Peso ideal
Entre 25 e 30 - Sobrepeso
Entre 30 e 40 - Obesidade
Acima de 40 - Obesidade morbida''')