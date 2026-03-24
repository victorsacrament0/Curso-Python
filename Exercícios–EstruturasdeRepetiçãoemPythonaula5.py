# 1-Mostre na tela os números de 1 a 10 usando for.

for num in range(1,11,1):  #(começo, final , passo(de quanto em quanto, intervalo) )
    print('Valor :' + str(num))
print('_' * 40)

#2-Mostre na tela os números de 10 a 1 (ordem decrescente)

for num in range(10,0,-1):  #(começo, final , passo(de quanto em quanto, intervalo) )  
    print('Valor :' + str(num))
print('_' * 40)

# 3- Exiba a tabuada do número 5 (de 1 a 10)

print('Tabuada do 5:')
for num in range(1,11,1):
    print(f'5 x {num} = {5 * num}')
print('_' * 40)

# 4-Exiba apenas os numeros pares de 1 a 20.

print('Numeros pares de 1 a 20:')   

for num in range(1,21):
    if num % 2 == 0:
        print('Numero par:' + str(num))
print('_' * 40)

# 5-Peça 5 números ao usuário e mostre a soma total.

soma_total = 0
for i in range(5):
    numero = float(input(f"Digite o {i}º número: "))
    soma_total += numero  
print(f"A soma total dos números é: {soma_total}")

"""
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
v3 = float(input('Digite o terceiro valor: '))
v4 = float(input('Digite o quarto valor: '))    
v5 = float(input('Digite o quinto valor: '))
soma = v1 + v2 + v3 + v4 + v5
print('_' * 40)
print(f'Valores digitados: {v1}, {v2}, {v3}, {v4}, {v5}')

print(f'Soma dos valores: {soma}')
print('_' * 40)"""

# 6-Peça números ao usuário até que ele digite 0. Ao final, mostre a soma de todos os números digitados.

soma = []
while True:
    num = int(input('Tente acertar o número secreto: '))
     

    if num == 0:
        print('_' * 40)
        print('Acertou o numero 0, programa encerrado! ')
        print('_' * 40)
        break  
    try:
        soma.append(num)  #append é um método de lista que adiciona um elemento ao final da lista. (acrescenta o numero digitado a lista soma)
        
    except ValueError:
     print('_' * 40)
     print('Valor invalido, digite um numero inteiro!')
     print('_' * 40)

total = sum(soma)   # sum =calcula a soma dos elementos de um iterável (listas, tuplas, conjuntos) de forma rápida. 
                    #Ela é ideal para somar números (inteiros ou floats), retornando o total da soma dos itens 
                    # mais um valor opcional inicial(padrão é iniciar em 0)
print(f"Números digitados: {soma}")
print(f"Soma dos números digitados: {total}")

#identação foi bastante usada! tava errando bastante a estrutura.

# 7-Peça a senha ao usuário até que ele acerte (senha = "1234").

senha = input('Digite a senha: ')

while senha != "1234":
    print('Senha incorreta, tente novamente!')
    senha = input('Digite a senha: ')
if senha == "1234":
        print('_' * 40)
        print('Senha correta, acesso permitido!')
        print('_' * 40)


# 8-Mostre a tabuada de um número escolhido pelo usuário.

try:
    print('_' * 40)
    num = int(input('Digite um numero para ver a tabuada: '))
    print('_' * 40)
    print(f'|Tabuada do {num}: |')
    print('_' * 40)
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
except ValueError:
    print('_' * 40)
    print('Por favor, digite um número válido.')
print('_' * 40)

#9

#10

# 11-Crie um programa que mostre todos os números pares entre dois números informados pelo usuário.

try:
    print('_' * 40)
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    print('_' * 40)
    print(f'|Números pares entre {n1} e {n2}: |')
    print('_' * 40)
    for i in range(n1, n2 + 1):
        if i % 2 == 0:
            print(i)
    print('_' * 40)        

except ValueError:
    print('_' * 40)
    print('Por favor, digite um número válido.')