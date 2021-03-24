import random
al1=str(input('nome do primeiro aluno: '))
al2=str(input('nome do segundo aluno: '))
al3=str(input('nome do terceiro aluno: '))
al4=str(input('nome do quarto aluno: '))
lista=[al1, al2, al3, al4]
esc=random.shuffle(lista)
print(lista)