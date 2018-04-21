from Usuario import Usuario

class Group(Usuario):
    def __init__(self,__login):
        super.__init__(__login)

    def despedidaGroup(self):
        print("A sessão está sendo encerrada .. ")

    def descreveGroup(self):
        ("Grupo permite o uso por grupo de usuários ..")

    def groupBoard(self):
        op = ""

        while(not (op == "s" or op == "n")):
            op = input("Ao apagar o grupo você apagará todos os usuários contidos nele, deseja prosseguir? [s/n] .. ")
            if(not op == "s" or not op == "s"):
                print("Entrada inválida, digite [s] para sim ou [n] para não ..")
            
        if(op.Lower() == "s"):
            ("Grupo deletado com sucesso!!")
        else:
            ("Operação cancelada!!")