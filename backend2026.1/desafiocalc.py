class Calculadora:
    def __init__(self,number1,number2):
        self.nu1 = number1
        self.nu2 = number2

    def somar(self):
        mensagem = f"\nResultado: {self.nu1} + {self.nu2} = {self.nu1 + self.nu2}\n"
        return mensagem 
    
    def subtrair (self):
        mensagem = f"\nResultado: {self.nu1} - {self.nu2} = {self.nu1 - self.nu2}\n"
        return mensagem 
    
    def dividir (self):
        mensagem = f"\nResultado: {self.nu1} ÷ {self.nu2} = {self.nu1 / self.nu2}\n"
        return mensagem 

    def multiplicar (self):
        mensagem = f"\nResultado: {self.nu1} x {self.nu2} = {self.nu1 * self.nu2}\n"
        return mensagem

    def main(self):
        while True:
            




numero = Calculadora(4,2)
numero.somar()
print(numero.dividir())