class Usuario:
    def __init__ (self, __login):
        self.__login = __login

    def _boasVindas(self):
        print("Bem-vindo ", self.__login)