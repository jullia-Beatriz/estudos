print('Ola! hoje eu sou o Detran!')
vel = int(input('Seu carro esta a quantos km/h? '))

if vel <= 80:
    print('')

else:
    if vel >=81:
        multa = (vel - 80) * 7
        print('Voce foi multado por excesso de velocidade!')
        print(f'PROCESSANDO [...] \nsua multa e no valor de: {multa} reais!')
