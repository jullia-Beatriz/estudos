km=float(input('quantos km o carro percorreu?: '))
d=int(input('quantos dias o carro ficou alugado?: '))
kmrod=km*0.15
diasa=d*60
print(' o carro rodou {} km por {} dias'.format(km, d))
print('voce tera que pagar {} por km e {} pelos dias alugados'.format(kmrod, diasa))
t=kmrod+diasa
print('isso da um valor total de: {:.2f}R$'.format(t))