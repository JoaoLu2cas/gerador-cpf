# calculo primeiro digito
import random

while True :
    opçao = input('Deseja gerar um CPF [s]im ou [n]ão ? : ').lower()
    if opçao == 'n' :
        print('Bye Bye')
        break
    elif opçao != 's' and 'n' :
        print('Insira uma das opções.')
        continue

    nove_digitos = ''
    for i in range(9) :
        nove_digitos += str(random.randint(0, 9))
    contador_regressivo = 10
    resultado_um = 0
     
    for digito in nove_digitos:
        resultado_um += int(digito) * contador_regressivo
        contador_regressivo -= 1
    
    digito_1 = (resultado_um * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    
    # calculo so segundo digito
    dez_digitos = ''
    contador_regr_dois = 11
    resultado_dois = 0
    
    for digito in dez_digitos :
        resultado_dois += int(digito) * contador_regr_dois
        contador_regr_dois -= 1
    
    digito_2 = (resultado_dois * 10 ) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    
    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
    print(cpf_gerado_pelo_calculo)
    continue

