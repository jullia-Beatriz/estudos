print('Ola, Seja bem vindo ao programa de emprestimos da CAIXA!')
print(' vamos fazer um orcamento ...')
casa = float(input('Digite o valor da casa: R$ '))
sal = float(input('Digite o seu salario: R$ '))
ano = int(input('Digite em quantos anos voce quer quitar a casa: '))
prestacao = casa / (ano * 12)
minimo = sal * 30 / 100
print(f'Para pagar uma casa de {casa} R$ em {ano} anos, a prestacao vai ser de: {prestacao} R$')

if prestacao <= minimo:
    print('O seu emprestimo esta LIBERADO!')
else:
    print('O seu emprestimo foi NEGADO!')

#FIQUEI BUGADA!!!!!