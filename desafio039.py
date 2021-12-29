age = int(input('Digite aqui seu ano de nascimento: '))
sex = int(input('''[1] Masculino
[2] Feminino
Digite aqui o número relacionado ao seu sexo: '''))
a_ant = 18 - 2021 - age
a_atr = 2021 - age - 18
if sex == 2:
    print('Você não precisa se alistar')
else:
    if 16 < (2021 - age) < 18:
        print('Você precisa se alistar esse ano!')
    elif (2021 - age) > 17:
        print(f'Você deveria ter se alistado a {a_atr} ano(s) atrás')
    elif (2021 - age) < 17:
        print(f'Você vai precisar se alistar daqui a {a_ant} ano(s)')
