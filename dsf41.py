from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento:  '))
idade = (atual - ano)

if idade <= 9:
    print('O atleta se encaixa na classificacao: MIRIM!')
elif idade <=14:
    print('O atleta se encaixa na modalidade: INFANTIL')
elif idade <=19:
    print('O atleta se encaixa na modalidade: JUVENIL!')
elif idade <=25:
    print ('O atleta se encixa na modalidade: SENIOR!') 
elif idade >25:
    print('O atleta se encainxa na modalidade: MASTER!')