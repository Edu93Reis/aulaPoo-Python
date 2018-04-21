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
        self.__saldo = __saldo

    def getLimite(self):
        return self.__limite

    def Sacar(self, __val):
        if(self.checarSaldo()>__val):
            self.__saldo -= __val
            return self.__saldo
        else:
            print(self.checarSaldo()," reais, saldo insuficiente para um saque neste valor!")
            return 0

    def retiraSaldo(self,__val):
        self.__saldo -= __val        
        return self.__saldo
    
    def aumentaSaldo(self,__val):
        self.__saldo += __val
        return self.__saldo

    def checarSaldo(self):
        return self.__saldo+self.__limite