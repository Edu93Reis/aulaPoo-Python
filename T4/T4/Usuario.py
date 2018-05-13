class Usuario:
    def __init__ (self, _login):
        self._login = _login

    def boasVindas(self):
        print("Bem-vindo,", self._login)

    def descreve(self):
        print("Bem Vindo: "+ self._login)
       
    
    def despedida(self):
        pass