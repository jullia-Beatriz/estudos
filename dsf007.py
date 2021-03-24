print('ola seja bem vindo(a)!')
n=input('qual e o nome do aluno(a) que vc quer calcular a media? ')
n1=float(input('digite a primeira nota: '))
n2=float(input('digite a segunda nota: '))
n3=float(input('digite a terceira nota: '))
n4=float(input('digite a quarta nota: '))
m=(n1+n2+n3+n4)/4
if  (m>=10):
    print(f'a media final e: {m:.2f}!', end='')
    print(f' O sistema foi burlado! e o aluno {n} reprovado!')
elif (m>=6):
    print('a media de corte e 6.0! o aluno(a) {} esta aprovado!'.format(n))
else:
    print('o aluno(a) {} esta reprovado'.format(n))