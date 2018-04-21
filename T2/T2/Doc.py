from Cliente import Cliente

class Doc:
    def __init__(self):
        pass

    def transferir(self, __c1, __c2, __quantia):
        if(__c1.checarSaldo()>=__quantia):
                __c2.setSaldo(__c2.aumentaSaldo(__quantia))
                __c1.setSaldo(__c1.retiraSaldo(__quantia))
                return __c2.getSaldo()
        else:
            print("Saldo insuficiente para transferência")
            return 0