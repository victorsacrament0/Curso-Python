valor1 = int(input('Digite um valor inteiro positivo: '))
valor2 = int(input('Digite outro valor inteiro positivo: '))
opm = input('Digite a operação matematica desejada: ')

def calc(valor1, valor2, opm):
    if opm =='+':
        resutado = valor1 + valor2
        return resutado
    elif opm == '-':
        resutado = valor1 - valor2
        return resutado
    elif opm == 'x':
        resutado = valor1 * valor2
        return resutado
    elif opm == '/':
        if valor2 == 0:
           mensagem = "Não é possivel divisão por ZERO"
           return mensagem
        else:
            resutado = valor1 / valor2
            return resutado
        
    
print(f'O resultado é : {calc(valor1, valor2, opm)}')