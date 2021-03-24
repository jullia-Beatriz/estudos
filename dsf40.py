#classicao media escolar
print('Ola! seja bem vindo!')
pri = float(input('Digite a primeira nota: '))
seg = float(input('Digite a segunda nota:  '))
ter = float(input('Digite a terceira nota: '))
media = (pri + seg + ter) / 3

if media == 6:
    print(f'A nota de corte e 7.0! \nSua media final foi de {media:.1f}! \nVoce esta de RECUPERACAO!')
elif media < 6:
    print(f'A nota de corte e 7.0! \nSua media final foi de {media:.1f}! \nVoce esta REPROVADO')
elif media > 7:
    print(f'A nota de corte e 7.0! \nSua media final foi de {media:.1f}! \nParabens voce esta APROVADO!')