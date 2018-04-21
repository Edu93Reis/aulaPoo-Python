from Usuario import Usuario

class Regular(Usuario):
    def __init__(self, __login):
        super.__init__(__login)

    def despedidaRegular(self):
        print("Até mais ", super.__login)

    def descreveRegular(self):
        print("Usuario Regular possui permissões intermediárias de uso do sistema ..")

    def dashboard(self):
        while(super.__login == Null or super.__login == ""):
            super.__login = String(input(Cadastre Login: ))            
           
            if(self.__login == "" or self.__login == Null):
                print("Campo login não pode ser valor vazio. Preencha login!")