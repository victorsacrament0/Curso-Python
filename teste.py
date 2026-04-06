matriz = [
    ['maçã','uva','pera','banana'],
    ['aguá','suco','mate'],
    ['coca','sprite','fanta']
]

matriz.append(['batata','hamburger','crepe'])
print(matriz)

matriz = [
    ['maçã','uva'],
    ['aguá','suco'],
]
print((matriz[0])+(matriz[1]))
print('') 
print(matriz [0][0])
print(matriz [0][1])
print(matriz [1][0])
print(matriz [1][1])
print('_' * 20)
for linha in matriz:
   for itens in linha:
       print(itens)