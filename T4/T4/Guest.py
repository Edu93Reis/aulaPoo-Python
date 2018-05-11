from Usuario import Usuario

class Guest(Usuario):
    def __init__(self, _login):
        super().__init__(_login)

    def despedida(self):
        print("Até mais", self._login)

    def descreve(self):
        print("Visitante possui permissões básicas de uso do sistema ..")