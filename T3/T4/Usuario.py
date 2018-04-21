class Usuario:
    def __init__ (self, __login):
        self.__login = __login

    def boasVindas(self):
        print("Bem-vindo ", self.__login)