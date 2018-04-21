from Usuario import Usuario

class Root(Usuario):
    def __init__(self, __login):
        super.__init__(__login)

    def despedidaRoot(self):
        print("Você está encerrando a sessão", super.__login, ", todos os usuarios serão encerrados automaticamente ..")

    def descreveRoot(self):
        print("Superusuário, possui o controle total do sistema")

    def descreverRoot(self):
        print("Superusuário, possui o controle total do sistema")

    def excluirTodos(self):
        op = input("Deseja realmente apagar todos os usuários? [s/n]")

        if(op.lower() == "s"):
            print("Usuários deletados com sucesso!!")
        else:
            print("Operação cancelada!")
