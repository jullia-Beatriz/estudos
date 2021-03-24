somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ' '
totmulher20 = 0
print('''
    Ola! seja bem vindo(A) ao sistema de analise de perfil!         
         ''')
for p in range(1, 5):
    print(f'_____ {p}* PESSOA _____')
    nome = input('nome:  ')
    idade = int(input('idade:  '))
    sexo = input('sexo: ')
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho =  nome
    if sexo in 'Mm'  and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome 
    if sexo in 'Fm' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A media idade do grupo e de {mediaidade} anos!')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}!')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos!')