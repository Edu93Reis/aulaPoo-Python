from Usuario import Usuario

class Regular(Usuario):
    def __init__(self, __login):
        super().__init__(__login)

    def __getlogin(self, __login):
        super.__getitem__(__login)

    def despedidaRegular(self):
        print("Até mais ", super.__login)

    def descreveRegular(self):
        print("Usuario Regular possui permissões intermediárias de uso do sistema ..")

    def dashboard(self):
        while(super().__login == Null or super().__login == ""):
            self.__getlogin = String(input(Cadastre Login: ))            
           
        if(__login == "" or __login == Null):
            print("Campo login não pode ser valor vazio. Preencha login!")