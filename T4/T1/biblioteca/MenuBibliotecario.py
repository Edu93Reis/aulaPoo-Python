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
               self.__b.criarEstante()

               option = self.escolherEstante()
               self.__b.getEstante(option).insereLivro(self.__b.getEstante(option).criaLivro())
            elif(__opt == 2):
                try:
                    self.MetodoException(BookNotFound)
                except BookNotFound as e:      
                    print()              
                    #print(e.getMessage())
            elif(__opt == 9):
                self.erro()
                
    def erro(self):
        print("Erro: opção inválida!")

    def escolherEstante(self):
        __opt = 0
        if(len(self.__b.getEstantes()) == 0):
            print("Não há estantes disponíveis na biblioteca")
            return -1
        else:
            __y = 0
            __x = 0
            while(__opt >= len(self.__b.getEstantes())):                                
                while(__x >= len(self.__b.getEstantes())):
                    print("Estante ",__y,": ", self.__b.getEstante(__x).getNome())
                    __y+=1
                    __x+=1
                    
                __opt = input("Escolha a estante: ")

                if(__opt >= len(self.__b.getEstantes())):
                    print("Estante inválida!")

        return __opt    
    
    def MetodoException(self, BookNotFound):
        __i = self.escolherEstante()
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
                self.__b.getEstante(__i).removeLivro(self.__b.getEstante(__i).getLivro(__livro))