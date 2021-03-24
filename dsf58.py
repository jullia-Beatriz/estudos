import random
nome = input('Ola seja bem vindo! qual e o seu nome? ')
print(f'''Ok {nome}! estou pensando em um numero entre 0 e 10!
vamos ver se voce consegue adivinhar. ''')
num = random.randrange(0,11)
cont = 1
adv = int(input('__ Chute um valor: __'))
while adv != num:
    cont += 1
    print(f'Voce errou tente novamente!')
    adv = int(input('__ Chute um valor: __'))
else:
    print(f''' Parabens {nome}! voce acertou com {cont} tentativas
    ate a proxima partida!''')
print(' ')