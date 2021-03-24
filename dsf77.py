palavras = (
    'APRENDER ....','PROGRAMAR ...','LINGUAGEM ...','PYTHON ......','CURSO .......','GRATIS ......',
    'ESTUDAR .....','PRATICAR ....','TRABALHAR ...','MERCADO .....','PROGRAMADOR .','FUTURO ......',

)

for lista in palavras:
    print(f'\nNa palavra {lista} temos as vogais: ',end='')
    for letra in lista:
        if letra.upper() in 'AEIOU':
            print(letra,end=' ')

print('''  
''')