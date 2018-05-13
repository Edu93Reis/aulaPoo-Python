from Usuario import Usuario

class Regular(Usuario):
    def __init__(self, _login):
        super().__init__(_login)

    def despedida(self):
        print("Até mais", self._login)

    def descreve(self):
        print("Usuario Regular possui permissões intermediárias de uso do sistema ..")

    def dashboard(self):
        self.__login = None

        while(self.__login == None):
            self.__login = input("Cadastre Login: ")            
            if(self.__login == None):
                print("Campo login não pode ser valor vazio. Preencha login!")
            else:
                print("Login cadastrado com sucesso")