from Biblioteca import Biblioteca
from Livro import Livro
from Estante import Estante
from Categoria import Categoria

class MenuGuest:
    def __init__(self):
        self.__b = Biblioteca("Principal")

    def menu(self):
        __opt = 0

        while(opt != 9):            
			print("Biblioteca")
			opt = input(print("Digite a opção: 1- Exibir Tudo, 9- Sair,")

            if(opt == 1):
               self.__b.criarestante()
            elif(opt == 9):
                self.erro()