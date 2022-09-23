class conta:
    def __init__(self,saldo=0):
        self._saldo = saldo

    def deposito(self,valor):
        self.valor += valor

    def saque(self,valor):
        self.valor -= valor

    def mostrae_saldo(self):
        return self._saldo


conta = conta(100)
conta.deposito(100)
print(conta.saldo)
print(conta.mostrae_saldo())