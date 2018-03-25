from Livros import Livros

class Produtos:
    __description = None

    def __init__(self):
        pass
    
    def setDescription(self, description):
        self.__description = str(description)

    def getDescription(self):
        if(self.__description == None):
            self.__description = str(input("Digite descricao do livro: "))
            return self.__description
        else:
            return self.__description

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getTipo(self):
        if(self.__tipo == Livros.Epub):
            return "Epub"
        elif(self.__tipo == Livros.Livro_Fisico):
            return "Livros Fisícos"
        elif(self.__tipo == Livros.PDF):
            return "PDF"

    def precoLivro(self, tipo):
        if(self.__tipo == Livros.Epub):
            self.__preco = 20.00
        elif(self.__tipo == Livros.PDF):
            self.__preco = 40.00
        else:
            self.__preco = 80.00
    
    def getPreco(self):
        if(self.__tipo == Livros.Epub):
            return self.__preco
        elif(self.__tipo == Livros.PDF):
            return self.__preco
        elif(self.__tipo == Livros.Livro_Fisico):
            return self.__preco
        else:
            print("Tipo de livro inexistente!")
            return 0
    