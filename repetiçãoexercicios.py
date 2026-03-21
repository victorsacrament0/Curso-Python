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