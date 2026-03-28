
    
total = 0
hamburger = 0
refri = 0
batata = 0

print('-----Seja bem vindo!------')
print('-Menu Restaurante Simples-')
print('_' * 30 + '\n' )
print('Nosso cardapio: \n Cardápio: \n Hamburguer - R$10 \n Refrigerante - R$5 \n Batata Frita - R$7  \n Digite [fim] para finalizar')
print('_' * 30 + '\n' )
try:
    while True:
        pedido = input("Digite o item desejado: ").lower()
        print('_' * 30 + '\n' )
        if pedido in ['fim' , 'finalizar' , 'sair']:
            break
        if pedido == 'hamburger':
            total += 10
            hamburger += 1
        elif pedido == 'refrigerante':
            total += 5
            refri += 1
        elif pedido in ['batata' , 'batata frita' , 'batatafrita']:
            total += 7
            batata += 1
        else:
            print('Valor Invalido')
            
        print(f'O pedido está dando = {total}')
except ValueError:
        print('\n')
        print ('Valor Invalido')
        print(('_' * 30) + '\n')

if total >= 20:
     total -= total * 0.1

print(f'Itens comprados: \n Hamburguer: {hamburger} \n Refrigerante: {refri} \n Batata Frita: {batata} \n')

print(f'Valor total do pedido = [R${total}] \n')

print('Obrigado por nos escolher, volte sempre!')
print('_' * 30 + '\n' )

