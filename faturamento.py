faturamento = {'Empresa1': 200500, 'Empresa2': 345600}

print('Relatoria Anual')
for key, value in faturamento.items():
    print('{0} possui um faturamento de {1:.2f}'.format(key, value))
    if value > 300000:
        print(f'{key} atende criterio de seleçao')


