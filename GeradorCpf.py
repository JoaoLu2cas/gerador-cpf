import random

while True :
    opçao = input('[g]erar um CPF, [v]álidar um CPF ou [e]xit : ').lower()
    if opçao == 'v' :
        entrada = input('Digite o CPF : ') \
            .replace('.', '')\
            .replace(' ', '')\
            .replace('-', '')
        soma_nove = entrada[:9]
        contador_regressivo = 10 
        
        resultado_digito_1 = 0
        
        for digito in soma_nove :
            resultado_digito_1 += int(digito) * contador_regressivo
            contador_regressivo -= 1
        digito_1 = (resultado_digito_1 * 10) %  11
        digito_1 = digito_1 if digito_1 <= 9 else 0
        
        soma_dez = soma_nove + str(digito_1)
        contador_regressivo_2 = 11
        
        resultado_digito_2 = 0
        for digito in soma_dez :
            resultado_digito_2 += (int(digito) * contador_regressivo_2)
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0 
        
        cpf_gerado_pelo_calculo = f'{soma_nove}{digito_1}{digito_2}'
        
        if entrada == cpf_gerado_pelo_calculo :
            print('CPF válido.')
            continue
        else :
            print('CPF inválido')
            break
    elif opçao =='e' :
        print('Bye Bye.')
        continue
    elif opçao != 'g' and 'e' :
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
    

    dez_digitos = nove_digitos + str(digito_1)
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