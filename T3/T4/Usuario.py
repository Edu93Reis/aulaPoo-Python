class Usuario:
    def __init__ (self, _login):
        self._login = _login

    def boasVindas(self):
        print("Bem-vindo,", self._login)