from datetime import date
atual = date.today().year
p = 0
ma = 0
me = 0

for c in range(1,8):
    p += 1
    nasc = int(input(f'Em que ano a {p}* pessoa nasceu?  '))
    idade = atual - nasc
    if idade >= 18:
        ma +=1
    else:
        me += 1

print(f'''  Ao todo tivemos {ma} pessoa(s) maiores de idade!
    E tambem tivemos {me} pessoa(s) menores de idade!''')