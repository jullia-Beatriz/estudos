print('Ola! Seja bem vindo(a) ao IMC!')
peso = float(input('Para comecarmos, Digite o seu peso (kg): '))
alt = float(input('Digite a sua altura (m):  '))
imc = peso / (alt * alt)
print(f' O  seu indice de massa corporal e {imc:.2f}.', end='')

if imc < 18.5:
    print('seja mais saudavel! Voce esta abaixo do peso!')
elif imc > 18.5 and imc < 24.9:
    print('parabens! Voce esta no peso normal!')
elif imc > 25 and imc < 29.9:
    print('se previna! Voce esta com sobrepeso!')
elif imc > 30 and imc < 34.9:
    print('Cuidado! Voce esta com obesidade grau 1!')
elif imc > 35 and imc < 39.9:
    print('Cuidado! Voce esta com obesidade grau 2!')
elif imc > 40:
    print('Cuidado! Voce esta com obesidade grau 3!')
