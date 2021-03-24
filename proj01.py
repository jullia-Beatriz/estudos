import random
nome = input('Ola seja bem vindo! qual e o seu nome? ')
print(f'''Ok {nome}! estou pensando em um numero entre 0 e 10!
vamos ver se voce consegue adivinhar. ''')
num = random.randrange(0,11)
cont = 1
adv = int(input(' Chute um valor: '))
while adv != num:
    cont += 1
    print(f'Voce errou tente novamente!')
    adv = int(input(' Chute um valor: '))
else:
    print(f''' Parabens {nome}! voce acertou com {cont} tentativas
    quer continuar jogando? ''')
    nov = int(input('''Sua resposta: [1 sim] [2 nao]  '''))
    num = random.randrange(0,11)
    cont = 0
    while nov !=2:
        if adv != num:
            cont += 1
            adv = int(input(' Chute um valor: '))
        elif adv == num:
            print(f'Parabens {nome}! voce ganhou!')
            break
    if nov == 2:
        print(f'Ok {nome}! ate a proxima partida!')

print(' ')