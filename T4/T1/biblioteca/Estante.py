from Livro import Livro

class Estante:
    def __init__ (self, __nome, __categoria):
        self.__nome = __nome
        self.__categoria = __categoria
        self.__livros = []

    def getNome(self):
        return self.__nome

    def getCategoria(self):
        return self.__categoria

    def getLivros(self):
        __y = 0        
        for livro in self.__livros:
            print("Livro:", __y)
            print("Título:", livro.getNome())
            print("Autor:", livro.getAutor())
            print("Ano:", livro.getAno())
            __y+=1

    def returnLivro(self):
        return self.__livros

    def getLivro(self, __nome):
        for livro in self.__livros:
            if(__nome in livro):
                print(livro)
    
    def getLivroIndex(self, __i):
        return self.__livros[__i]

    def listaLivros(self):
        for livro in self.__livros:
            return livro

    def removeLivro(self, __livro):
        self.__livros.remove(__livro)

    def insereLivro(self, __livro):
        self.__livros.append(__livro)

    def criaLivro(self):
        __nome = input(print("Insira o título do livro:"))
        __autor = input(print("Insira o nome do autor: "))
        __ano = 0
        while __ano > 2018:
            __ano = max(0, input(print("Insira o ano de publicação do livro:")))			
            if (__ano > 2018):
                print("Ano inválido")
                
        l = Livro(__nome,__autor,__ano)
        return l