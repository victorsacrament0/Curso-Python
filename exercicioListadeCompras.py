lista = []
lista_alf = sorted(lista)

while True:
    try:   
       print('_'*60 +'\n')
       print('        ---Bem Vindo a lista de compras Python---') 
       print('    ---Digite o numero referente a operação desejada---\n')
       print('1-Adicionar | 2-Remover | 3-Listar | 4-Quantidade | 5-Sair \n')
       prod = int(input('Digite a opção desejada: '))
       print('_'*60 +'\n')
       if prod < 1 or prod > 5:
           print('Valor Inválido!\n')
           continue
       if prod == 1:
           item = input('Digite o produto desejado: ')
           lista.append(item)
       elif prod == 2:
           rem = input('Digite o produto que deseja remover: ')
           lista.remove(rem)
       elif prod == 3:
           print(lista_alf)
       elif prod == 4:
           qnt = len(lista)
           print(f'Quantidade de intens na sua lista: {qnt}')
       elif prod == 5:
           print('---Fim---')
           break
       else:
           print('Digite um item válido\n')
           continue

    except ValueError:
        print('_' * 60)
        print('Erro! Parametro inválido.')
    
print(f'Sua lista de compras foi: {lista_alf}\n')
print('Obrigado por nos escolher! Volte Sempre!')
print('_' * 60 , '\n')


#para permitir remover um item numa determinada posição, usamos o lista.pop(0), remove indicando a posição na lista
#para permitir adicionar um item em um locar especifico na lista usamos o lista.insert(0, "itemdesejado")