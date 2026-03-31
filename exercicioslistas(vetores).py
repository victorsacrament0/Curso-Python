# 1 - Crie um vetor com 5 números e mostre todos na tela.
lista = ['n1','n2','n3','n4','n5']


for item in lista:
    print(f'Numero da lista: {i}')

# 2 - Crie um vetor com 3 nomes e exiba o primeiro e o último.

lista = ['n1','n2','n3']

primeiro = lista[0]
ultimo = lista[-1]

print(f'O primeiro numero é: {primeiro} e o ultimo é: {ultimo} ')

# 3 - Crie um vetor e mostre seu tamanho.

lista = ['n1','n2','n3']
tamanho = len(lista)
print(f'Tamanho = {tamanho}' )

# 4 - Crie dois vetores e concatene eles.

lista1 = ['n1','n2','n3']
lista2 = ['n4','n5','n6']
con = lista1 + lista2

print(f"Resultado da concatenação: {con}")