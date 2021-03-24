from time import sleep
print('OLa! seja bem vindo! \nDeseja inicar a contagem regressiva agora?')
fogos = int(input('[1] Sim   [2] Nao   \n  resposta:  '))

if fogos == 1:
    c = 0
    for c in range(100000,-1, -5):
        print(c)
    print('   FELIZ ANO NOVO!!')
else: 
    print('OK! Ate breve!')