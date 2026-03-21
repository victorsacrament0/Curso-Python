num = 0

while num < 10:
    print('Decrescente: ' + str(num))
    num += 1

'''----------------------'''
for num in range(0,10,2):  #(começo, final , passo(de quanto em quanto, intervalo) )
    print('Varlor :' + str(num))

# Calcular imposto de produtos e calcular eles (imposto para valores maiores q 1000 de 15% e ate mil 10%)
lista_preco = [1200,1000,1500,800]
total_imposto = 0

for preco in lista_preco:
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = taxa * preco

    total_imposto += imposto
    print(f'Valor do produto: {preco} com imposto de {imposto}')

print('Total dos impostos é', total_imposto )


#Usar o for num dicionario: calcular o percentual de crescimento
#calculo valor / valor2 - 1 - procentagem de crescimento de um ano pro outro

vendas23 = {'jan': 15000, 'fev':12000,'mar':13500}
vendas24 = {'jan': 16000, 'fev':13000,'mar':12000}

for mes in vendas24:
    valor23 = vendas23[mes]
    valor24 = vendas24[mes]
    crescimento = valor24 / valor23 - 1
    print(f'No mes de {mes} o crescimento foi de {crescimento:.1%}') 
                                             #.1$ retorna quantas casas vc quer dps do . e % o tipo que deseja