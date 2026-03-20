senha = input('Digite a senha: ')

while senha != "1234":
    print('Senha incorreta, tente novamente!')
    senha = input('Digite a senha: ')
if senha == "1234":
        print('_' * 40)
        print('Senha correta, acesso permitido!')
        print('_' * 40)
