print('ola seja bem vindo!')
nome=input('qual e o nome do aluno(a) que voce gostaria de calcular a media?  ')
h=float(input('ok! me informe a nota na disciplina de historia: '))
p=float(input('me informe agora a nota em portugues: '))
m=float(input('me informe a nota em matematica: '))
m=h+p+m
m=m/3
print('a media final do aluno(a) {} e {}'.format(nome, m))
corte=input('a media de corte e 6.0, {} esta aprovado(a)? '.format(nome))