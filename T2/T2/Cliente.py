class Cliente:
    def __init__(self, __nome, __saldo, __limite):
        self.__nome = __nome
        self.__saldo = __saldo
        self.__limite = __limite

    def getNome(self):
        return self.__nome

    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, __saldo):
        self.__saldo = max(0, __saldo)

    def getLimite(self):
        return self.__limite

    def Sacar(self, val):
        if(self.checarSaldo()>val):
            self.__saldo -= val
            return self.__saldo
        else:
            print(self.checarSaldo()," reais, saldo insuficiente para um saque neste valor!")
            return 0

    def checarSaldo(self):
        return self.__saldo+self.__limite