from Usuario import Usuario

class Root(Usuario):
    def __init__(self, _login):
        super().__init__(_login)
        
    def excluirTodos(self):
        op = input("Deseja realmente apagar todos os usuários? [s/n]")

        if(op.lower() == "s"):
            print("Usuários deletados com sucesso!!")
        else:
            print("Operação cancelada!")

    def despedida(self):
        print("Você está encerrando a sessão", self._login, ", todos os usuarios serão encerrados automaticamente ..")

    def descreve(self):
        print("Superusuário, possui o controle total do sistema")
