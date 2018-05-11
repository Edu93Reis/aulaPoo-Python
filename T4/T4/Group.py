from Usuario import Usuario

class Group(Usuario):
    def __init__(self,_login):
        super().__init__(_login)

    def despedida(self):
        print("A sessão está sendo encerrada .. ")

    def descreve(self):
        ("Grupo permite o uso por grupo de usuários ..")

    def groupBoard(self):
        op = ""

        while(not (op == "s" or op == "n")):
            op = input("Ao apagar o grupo você apagará todos os usuários contidos nele, deseja prosseguir? [s/n] .. ")
            if(not op == "s" or not op == "s"):
                print("Entrada inválida, digite [s] para sim ou [n] para não ..")
            
        if(op.lower() == "s"):
            ("Grupo deletado com sucesso!!")
        else:
            ("Operação cancelada!!")