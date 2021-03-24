from datetime import date
atual = date.today().year

print('Ola seja bem vindo ao programa de alistamento do governo!')
print('Selecione seu genero: \n[1] MASCULINO \n[2] FEMININO')
gene = int(input('Digite sua resposta:  '))
if gene == 1:
    print('OK! vamos continuar o processo!')
    ano = int(input('Digite o ano de nascimento:  '))
    idade = (atual - ano)
    alist = (idade - 18)

    print(f'Quem nasceu em {ano} atualmente completa {idade} anos')
    if idade == 18:
        print('Voce esta na idade certa para se alistar! Boa Sorte!')
    elif idade < 18:
        print(f'Sem pressa! ainda faltam {alist} ano(s) para voce se alistar!')
    elif idade > 18:
        print(f'voce esta {alist} ano(s) atrasado! seu alistamento foi em {atual - alist}!')

elif gene == 2:
    print('Voce nao precisa se alistar! Tenha um bom dia!')