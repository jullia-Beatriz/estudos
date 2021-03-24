pri=int(input('digite um numero:  '))
sec=int(input('digite outro valor: '))
a=pri+sec
m=pri*sec
d=pri/sec
di=pri//sec
e=pri**sec
print(' A soma e {},\n a multiplicacao e {},\n a divisao dos valores e {:.3f}'.format(a, m, d),  end=' ')
print('\n a divisao inteira e {},\n a potenciacao e {}'.format(di, e))
