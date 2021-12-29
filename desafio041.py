year = int(input('Digite aqui o ano de nascimento do atleta: '))
age = 2021 - year
if age <= 9:
    print('O atleta está na categoria MIRIM!')
elif 9 < age <= 14:
    print('O atleta está na categoria INFANTIL!')
elif 14 < age <= 19:
    print('O atleta está na categoria JUNIOR!')
elif 19 < age <= 20:
    print('O atleta está na categoria SÊNIOR!')
else:
    print('O atleta está na categoria MASTER!')