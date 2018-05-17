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

               option = self.escolheEstante()
               self.__b.getEstante(option).insereLivro(self.__b.etEstante(option).criaLivro())
            elif(__opt == 2):
                try:
                    self.MetodoException
                except Exception(BookNotFound e):
                    print(e.getMessage())
            elif(__opt == 9):
                self.erro()

	def erro(self):
        print("Erro: opção inválida!")

    def escolherEstante(self):
        __opt

        if(len(b.getEstante()) == 0):
            print("Não há estantes disponíveis na biblioteca")
            return -1
        else:
            while(__opt >= len(b.getEstante())):
                __y = 0
                for(estante in b.getEstante()):
                    print("Estante ",__y,": ",b.estante.getNome())
                    __y++
                    
                __opt = input("Escolha a estante: ")

                if(__opt >= len(b.getEstante())):
                    print("Estante inválida!")

        return __opt    
        
	def BookNotFound(self, Exception):
		__i = self.escolheEstante()
		__livro
		if(len(b.getEstante(i).getLivro())==0)
			print("Não há livros para excluir")
		else:
			print("Escolha o livro para excluir:")
				b.getEstante(i).getLivros()
				__livro = input("Dgite livro escolhido: ")
					if(__livro<0 or __livro > i):
						throw BookNotFound("Livro não encontrado")					
					else
						b.getEstante(i).removeLivro(b.getEstante(i).getLivro(livro))