from Usuario import Usuario

class Guest(Usuario):
    def __init__(self, __login):
        super.__init__(__login)

    def despedidaGuest(self):
        print("Até mais ", super.__login)

    def descreveGuest(self):
        print("Visitante possui permissões básicas de uso do sistema ..")