from time import sleep
from random import randint
itens =('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)

print('''Bem vindo ao Jokenpo! abaixo suas opcoes:
 [0] Pedra 
 [1] Papel
 [2] Tesoura''')
jogador = int(input('Digite suas jogada: '))

r = 'Nao'
r = r.istitle()
while r != 'Nao':
    if jogador == 0:
        if computador == 0:
            print(f'O computador jogou  {itens[computador]}\nO jogador jogou  {itens[jogador]}\n ... EMPATE!')
        elif computador == 1:
            print(f' O computador jogou  {itens[computador]}\nO jogador jogou  {itens[jogador]}\n ...VOCE PERDEU!')
        elif computador == 2:
            print(f' O computador jogou  {itens[computador]}\nO jogador jogou  {itens[jogador]}\n ...VOCE GANHOU!')

    elif jogador == 1:
        if computador == 0:
            print(f' O computador jogou  {itens[computador]}\nO jogador jogou  {itens[jogador]}\n ...VOCE GANHOU!')
        elif computador ==1:
            print(f' O computador jogou  {itens[computador]}\nO jogador jogou  {itens[jogador]}\n ... EMPATE!')
        elif computador == 2:
            print(f' O computador jogou  {itens[computador]}\nO jogador jogou  {itens[jogador]}\n ...VOCE PERDEU!')

    elif jogador == 2:
        if computador == 0:
            print(f' O computador jogou  {itens[computador]}\nO jogador jogou  {itens[jogador]}\n ...VOCE PERDEU!')
        elif computador == 1:
            print(f' O computador jogou  {itens[computador]}\n  jogador jogou  {itens[jogador]}\n ...VOCE GANHOU!')
        elif computador == 2:
            print(f' O computador jogou  {itens[computador]}\nO jogador jogou  {itens[jogador]}\n ... EMPATE!')
    else:
        print('opcao invalida! Deseja jogar novamente? [Sim/Nao]')