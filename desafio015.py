days = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
fp = days*60+km*0.15
print(f'O valor total é de R${fp:.2f}')