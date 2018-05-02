class Livro:
    def __init__(self, __nome, __autor, __ano):
        self.__nome = __nome
        self.__autor = __autor
        self.__ano = __ano

    def getNome(self):
        return self.__nome
    
    def getAutor(self):
        return self.__autor

    def getAno(self):
        return self.__ano