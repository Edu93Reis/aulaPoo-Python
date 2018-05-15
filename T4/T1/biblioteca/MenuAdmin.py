from Biblioteca import Biblioteca
from Livro import Livro
from Estante import Estante
from Categoria import Categoria
from BookNotFound import BookNotFound

class Menu(BookNotFound):
    def __init__(self):
        self.__b = Biblioteca("Principal")

    def menu(self):
        __opt = 0
        while(__opt != 9):            
            print("Controle de Biblioteca")
            __opt = input(print("Digite a opção: 1- Inserir Estante, 9- Sair")
            
                if(opt == 1):
                   self.__b.criarestante()
            elif(opt == 2):
                option = self.escolheEstante()
                self.__b.getEstante(option).insereLivro(self.__b.etEstante(option).criaLivro())
            elif(opt == 3):
                self.__b.listarTudo()
            elif(opt == 4):
                i = self.escolheEstnate()
                if(i == -1):
                    break
                int livro;
					if(b.getEstante(i).getLivro().size()==0):
						print("Não há livros para excluir")
					else:
						while(livro >= b.getEstante(i).getLivro().size()):
							print("Escolha o livro para excluir:");
							b.getEstante(i).getLivros()
							livro = max(0,input("Digite Escolha: "))
								if (livro >= b.getEstante(i).getLivro().size()):
									print("Livro inválido")								
								else:
									b.getEstante(i).removeLivro(b.getEstante(i).getLivro(livro))								
								
            elif(opt == 5):
                print(self.__b.contarCiencia())
            elif(opt == 6):
                
            elif(opt == 7):
                cat = self.__b.escolherCategoria()
                for(int w = 0; w < b.listarAutores(cat).size(); w++):
                    print(self.__b.listarAutores(cat).get(w))
            elif(opt == 8):
                print("Fim...")
            elif(opt == 9):
                self.erro()

def erro(self):		
	print("Erro: Opção inválida")
	
def escolheEstante(self):
    __opt
	if (b.getEstante().size() == 0):
        print("Não há estantes disponíveis na biblioteca.")
		return -1
	else:
		while(len(opt >= b.getEstante()):
                __y = 0
				print("Escolha a estante:")
				for (estante in Estante()):
					print("Estante " + y + ":" + b.estante.getNome())
					y++
	
				opt = Math.max(0, input("Digite opção: "));
				if (opt >= len(b.getEstante())):
					print("Estante inválida.")
			
		return opt
	
	def MetodoException(Exception):
		__i = self.escolheEstante()
		__livro
		
        if(len.(getEstante(i).getLivro())==0):
			print("Não há livros para excluir")
		else:
			print("Escolha o livro para excluir:")
			b.getEstante(i).getLivros()
			livro = input(print("Digite sua opção"))
					if(livro<0 or livro > i):
						throw BookNotFound("Livro não encontrado")
                        #BookNotFound("Livro não encontrado")
					else:
						b.getEstante(i).removeLivro(b.getEstante(i).getLivro(livro))
