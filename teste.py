usuario_correto = "admin"
senha_correta = "1234"
print('|Login Simples|')
print('Digite seu usuário e senha para acessar o sistema.')
print('_' * 30 + '\n' )
usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')
if usuario == usuario_correto and senha == senha_correta:   
    print('_' * 30 + '\n' )  
    print('-Login bem-sucedido-')
else:
    print('_' * 30 + '\n' )  
    print('-Usuário ou senha incorretos-')

print('_' * 30 + '\n' )  
