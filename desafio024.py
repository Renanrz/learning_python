city = str(input('Digite o nome de uma cidade: ')).strip()
list = city.split()
list[0].find('SANTO')
if list[0].upper().find('SANTO') == 0:
    print('O nome da cidade começa com Santo')
else:
    print('O nome da cidade não começa com Santo')