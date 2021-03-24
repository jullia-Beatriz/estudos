import random
nome = input('Ola seja bem vindo! qual e o seu nome? ')
print(f'seja bem vindo(A)! {nome}\nestou pensando em um numero entre 0 e 100 [...]')
num = random.randrange(0,11)
print('vamos ver se voce consegue adivinhar. ')
adv = input('chute um valor: ')
if adv == num:
    print('Parabens!! voce acertou!')
else:
    print(f'errou! era {num}. Mais sorte na proxima! ')