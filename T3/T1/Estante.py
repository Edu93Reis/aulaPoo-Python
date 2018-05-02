from Livro import Livro

class Estante:
    def __init__ (self, __nome, __categoria):
        self.__nome = __nome
        self.__categoria = __categoria
        self.livros = []

    def getNome(self):
        return self.__nome

    def getCategoria(self):
        return self.__categoria

    def getLivros(self):
        y = 0
        for(livro in self.__livros):
            print("Livro:", y)
            print("Título:", livro.__getNome())
            print("Autor:", livro.__getAutor())
            print("Ano:", livro.__getAno())
            y++
    
    def getLivro(self):
        return self.__livros

    def getLivro(self):
        for(livro in self.__livros):
            

    