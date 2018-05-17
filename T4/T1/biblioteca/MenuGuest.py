from Biblioteca import Biblioteca
from Livro import Livro
from Estante import Estante
from Categoria import Categoria

class MenuGuest:
    def __init__(self):
        self.__b = Biblioteca("Principal")

    def menu(self):
        __opt = 0

        while(__opt != 9):
            print("Biblioteca")
            __opt = input(print("Digite a opção: 1- Exibir Tudo, 9- Sair,"))
            
            if(__opt == 1):
               self.__b.criarEstante()
            elif(__opt == 9):
                self.erro()

    def erro(self):
        print("Erro: opção inválida!")