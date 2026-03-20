print(('_' * 30 ) + '\n')
print('--Jogo da adivinhação--')
print(('_' * 30) + '\n')
print('Descubra o valor secreto')
print(('_' * 30) + '\n')

import random

try:

    n_certo = random.randint(10,100)

    num = int(input('Digite um numero entre 10 e 100: ' ))
    print(f"-Você digitou: ({num})-")
    print(('_' * 30) + '\n')
   
    if num < 10 or num > 100:
        print(f"[ERRO] Tente um número entre 10 e 100. Digitado:({num})")
    elif num == n_certo:
        print('\n')
        print(('- Acertou Miseravi -') + '\n') 
        print(('_' * 30) + '\n')
    elif num < n_certo:
        print('\n')
        print((f'- Quase lá, mas este valor ainda é menor que o desejado!- R:({n_certo})') + '\n')
        print(('_' * 30) + '\n')
    else:
        print('\n')
        print((f'- Quase lá, mas este valor é maior que o desejado!- R:({n_certo})') + '\n')
        print(('_' * 30) + '\n')
except ValueError:
    print('\n')
    print ('Valor Invalido')
    print(('_' * 30) + '\n')

  
    # try - except - servem para fazer tratamento de erros
    # RANDOM: começar sempre com import random (importar a biblioteca do random)
    # random.randrange(0,5) = 0,1,2,3 e 4
    # random.randint(0,5) = 0,1,2,3,4 e 5
    # random.choices(variaveis) seleciona múltiplos elementos aleatórios de uma sequência (lista, tupla, etc.) com reposição
    # random.shuffle(variaveis) rearranja os elementos da lista fornecida em uma ordem aleatória.
    # random.sample  é utilizada para selecionar aleatoriamente um número específico de itens únicos de uma sequência
    # random.random  é utilizada para gerar um número de ponto flutuante (float) 
    #      pseudo-aleatório no intervalo de 0.0 (inclusive) a 1.0 (exclusivo), ou seja, [0.0, 1.0)
    # .2f = indica que o número deve ser exibido com 2 casas decimais