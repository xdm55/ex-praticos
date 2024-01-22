salario = float(input('digite o salario bruto: '))

# dicionário percentual de desconto
fdesc = {0: 0.0, 1: 7.5, 2: 15.0, 3: 22.5, 4: 27.5}

# dicionário valor padrão
fvpad = {0: 0.0, 1: 142.80, 2: 354.80, 3: 636.13, 4: 869.36}

if salario <= 1903.98:
    faixa = 0
elif salario >=1903.98 and salario <= 2826.65:
    faixa = 1
elif salario >= 2826.65 and salario <= 3751.05:
    faixa = 2
elif salario >= 3751.05 and salario <= 4664.68:
    faixa = 3
else:
    faixa = 4

imposto = salario*(fdesc[faixa]/100)
vpad = fvpad[faixa]
impagar = imposto - vpad
liquido = salario - impagar

mensagem_1 = 'Bruto: %10.2f, Faixa: %d, Imposto: %5.2f' % (salario,faixa,imposto)
mensagem_2 = 'Padrão: %5.2f, Pagar: %5.2f, Liquido: %5.2f' % (vpad,impagar,liquido)
print(mensagem_1)
print(mensagem_2)
