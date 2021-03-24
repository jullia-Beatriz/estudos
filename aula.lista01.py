lanche = ['hamburguer','suco','pizza','pudim']

# como adicionar itens:
lanche.append('biscoito') #adiciona no final da lista
lanche.insert(0,'cachorro quente') #adiciona no indice 0

# como deletar itens:
del lanche[3] #deleta o item 3
lanche.pop(3) #normalmente deleta o ultimo item,+ pode passar indice
lanche.remove('pizza') # elimina pelo conteudo, nao pela chave
if pizza in lanche:
    lanche.remove('pizza') #para testar se a pizza ta na lista IF IN 

#como declarar uma lista: funcao LIST
valores = list(range(4,11)) #gera uma lista no intervalo de 4 a 10
valor = [8,2,5,4,9,3,0] #gerando uma lista aleatoria
valor.sort() #reordena a lista em ordem crescente
valor.sort(reverse=True) #reordena a lista em ordem inversa
len(valores) #ler quantos elementos tem a lista

#EXEMPLO:
valores = ()
valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor:  ')))

a = [2,3,4,7]
b = a[:] #criar uma copia dos itens

a = [2,3,4,7]
b = a # criar um aligacao