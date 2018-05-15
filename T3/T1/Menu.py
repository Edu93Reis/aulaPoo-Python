from Biblioteca import Biblioteca
from Livro import Livro
from Estante import Estante
from Categoria import Categoria

class Menu:
    def __init__(self):
        self.__b = Biblioteca("Principal")

    def menu(self):
        __opt = 0

        while(opt != 9):            
			print("Controle de Biblioteca")
			opt = input(print("Digite a opção: 1- Inserir Estante, 2- Inserir Livro, 3- Exibir tudo, 4- Remover Livro, 5- Contar livros de Ciência, 6- Exibir livros de Filosofia, 7- Listar autores, 9- Sair,")

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
					if(b.getEstante(i).getLivro().size()==0)
						System.out.println("Não há livros para excluir");
					else {
						do {
							System.out.println("Escolha o livro para excluir:");
							b.getEstante(i).getLivros();
							livro = Math.max(0,s.nextInt());
								if (livro >= b.getEstante(i).getLivro().size()) {
									System.out.println("Livro inválido");
								}
								else {
									b.getEstante(i).removeLivro(b.getEstante(i).getLivro(livro));
									break;
								}
						}
						while (livro >= b.getEstante(i).getLivro().size());
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
			
			