from Biblioteca import Biblioteca
from Livro import Livro
from Estante import Estante
from Categoria import Categoria

class MenuBibliotecario:
    def __init__(self):
        self.__b = Biblioteca("Principal")

    def menu(self):
        __opt = 0

        while(opt != 9):            
			print("Controle de Biblioteca")
			opt = input(print("Digite a opção: 1- Inserir Livro, 2- Remover Livro, 9- Sair,")

            if(opt == 1):
               self.__b.criarestante()
            elif(opt == 2):
                option = self.escolheEstante()
                self.__b.getEstante(option).insereLivro(self.__b.etEstante(option).criaLivro())
            elif(opt == 9):
                self.erro()

			