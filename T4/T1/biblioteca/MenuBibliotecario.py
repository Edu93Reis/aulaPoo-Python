from Biblioteca import Biblioteca
from Livro import Livro
from Estante import Estante
from Categoria import Categoria
from BookNotFound import BookNotFound

class MenuBibliotecario(BookNotFound):
    def __init__(self):
        self.__b = Biblioteca("Principal")

    def menu(self):
        __opt = 0

        while(__opt != 9):            
            print("Controle de Biblioteca")
            __opt = input(print("Digite a opção: 1- Inserir Livro, 2- Remover Livro, 9- Sair,"))
            
            if(__opt == 1):
               self.__b.criarestante()

               option = self.__b.escolheEstante()
               self.__b.getEstante(option).insereLivro(self.__b.estante(option).criaLivro())
            elif(__opt == 2):
                try:
                    self.MetodoException()
                except BookNotFound as e:
                    print(e.getMessage())
            elif(__opt == 9):
                self.erro()
                
    def erro(self):
        print("Erro: opção inválida!")

    def escolherEstante(self):
        __opt

        if(len(self.__b.getEstante()) == 0):
            print("Não há estantes disponíveis na biblioteca")
            return -1
        else:
            while(__opt >= len(self.__b.getEstante())):
                __y = 0
                for estante in self.__b.getEstante():
                    print("Estante ",__y,": ", self.__b.estante.getNome())
                    __y+=1
                    
                __opt = input("Escolha a estante: ")

                if(__opt >= len(self.__b.getEstante())):
                    print("Estante inválida!")

        return __opt    
    
    def MetodoException(self, BookNotFound):
        __i = self.escolheEstante()
        __livro = 0
        if(len(self.__b.getEstante(__i).getLivro())==0):
            print("Não há livros para excluir")
        else:
            print("Escolha o livro para excluir:")
            self.__b.getEstante(__i).getLivros()
            
            __livro = input("Dgite livro escolhido: ")
            if(__livro < 0 or __livro > __i):
                raise BookNotFound("Livro não encontrado")					
            else:
                self.__b.getEstante(__i).removeLivro(self.__b.getEstante(i).getLivro(__livro))