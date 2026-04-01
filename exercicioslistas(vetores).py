# 1 - Crie um vetor com 5 números e mostre todos na tela.
lista = ['n1','n2','n3','n4','n5']


for i in lista:
    print(f'Numero da lista: {i}')

# 2 - Crie um vetor com 3 números e exiba o primeiro e o último.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
lista = [n1, n2 , n3]

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

# 5 - Crie um vetor e mostre apenas parte dele usando slice.

lista = [10,20,30,40,50,60,70,80,90]
print(lista[2:5])

# 6 - Crie um vetor e adicione um elemento em posição específica.

lista = ['uva', 'maçã', 'pera']

fruta = input('Digite uma fruta: ')
lista.append(fruta)
print(lista)

# 7 - Crie um vetor e remova um elemento usando pop()

lista = ['uva', 'maçã', 'pera']

lista.pop(-1) #colocar o passo
print(lista)

# 8 - Crie uma matriz com 3 linhas e mostre seu tamanho.

matriz = [
    ['maçã','uva','pera','banana'],
    ['aguá','suco','mate'],
    ['coca','sprite','fanta']
]

linhas = len(matriz)
print(f'Linhas: {linhas}')
print('_' * 40)

# Número de colunas (assumindo que todas as linhas têm o mesmo tamanho)
colunas = len(matriz[0]) if linhas > 0 else 0
print(f'Colunas: {colunas}')

# 9 - Crie uma matriz e insira uma nova linha em posição específica.

matriz = [
    ['maçã','uva','pera','banana'],
    ['aguá','suco','mate'],
    ['coca','sprite','fanta']
]

matriz.append(['batata','hamburger','crepe'])
print(matriz)

# 10 - Crie uma matriz 3x3 e mostre a soma dos elementos e a diagonal principal.

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

soma = (matriz[0])+(matriz[1])+(matriz[2])
print('\nA soma dos elementos é de: {}'.format(soma)) 
print('_' * 40, '\n')

diagonal = [matriz[i][i] for i in range(len(matriz))]

print("Matriz:")
for linha in matriz:
    print(linha)

print("\nDiagonal principal:", diagonal,'\n')


#extras
#mostrar 6 numeros e qm é o maior e o menor
#lista = [10,20,30,40,50,60]
#print(lista)
#print(f'O maior numero é: {max(lista)}')
#print(f'O menor numero é: {min(lista)}')


############################
#pedir 4 numeros e mostrar a soma e media
soma = 0
numero = 0
numeros = []  

for i in range(4):
    numero = int(input("Informe um numero : "))
    soma = soma + numero
    numeros.append(numero)  

media = len(numeros)

print(f'Números digitados: {numeros}') 
print(f"Soma: {soma} ")
print(f'Media:{soma / media}')

#ALTERNATIVA COM O sum()
#numeros = []
 
#for i in range(4):
#    n = int(input("Digite os números: "))
#    numeros.append(n)
#print("Números digitados foram:", numeros)
#soma = sum(numeros)  
#print("Soma dos números é:", soma)
#media = soma / len(numeros)
#print("Média dos números é:", media)
 
 