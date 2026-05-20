class ContaBancaria:
    def __init__(self,saldo,deposito):
        self.saldob = saldo
        self.depo = deposito

    def info_saldo(self):
        print(f'O saldo é de  R${self.saldob}')

    def info_dep(self):
        if self.depo > 0:
            print(f'O deposito foi de R${self.depo}')
        else:
            print(f'Apenas depositos de valores positivos')

operacao = ContaBancaria(1000,500)
operacao.info_saldo()
operacao.info_dep()