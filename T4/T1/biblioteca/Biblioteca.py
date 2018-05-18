from Estante import Estante
from Livro import Livro
from Categoria import Categoria

class Biblioteca:
    
    def __init__(self, __nome):
        self.__nome = __nome
        x = Estante("1", Categoria.Categoria.Filosofia)
        y = Estante("2", Categoria.Categoria.Ciência)
        self.__estante = [x, y]
        a = Livro("Exemplo 1", "Autor 1", 1999)
        b = Livro("Exemplo 2", "Autor 2", 1997)
        x.insereLivro(a)
        y.insereLivro(b)

    def getNome(self):
        return self.__nome

    def getEstante(self, i):
        if(self.__estante is not None):
            return self.__estante[i]

    def getEstantes(self):
        if(self.__estante is not None):
            for estante in self.__estante:
                return estante
        else:
            pass

    def inserirEstante(self, __estante):
        if(self.__estante is not None):
            self.__estante.append(__estante)
        else:
            print("Entre com valor válido")

    def criarEstante(self):
        __nome = ""
        __categoria = ""
        while(__nome == "" or __categoria == ""):
            __nome = input(print("Digite o nome da estante: "))
            
            if(__nome == ""):
                print("Preencha o nome")
            else:
                print("Insira a categoria da estante: ")
                __categoria = self.escolherCategoria() 
                __e = Estante(__nome, __categoria)
                self.inserirEstante(__e)
                print("Estante criada com sucesso")
    
    def listarfilosofia(self):
        __novo = []
        __i = 0
        for estante in self.__estante:
            if(estante.getCategoria() == Categoria.Categoria.Filosofia):
                __novo.append(estante).livro.returnLivro()
                #while __i < len(estante.returnLivro()):
        return __novo

    def contarCiencia(self):    
        __cont = 0
        for estante in self.__estante:
            if(estante.getCategoria() == Categoria.Categoria.Ciência):
                __cont = __cont + len(estante.returnLivro())
        return __cont

    def listarAutores(self):
        lista = []
        __x = 0
        if(self.__estante == None):
            print("Não há Estantes!")
        else:
            for estante in self.__estante:
                if(estante.getCategoria() == Categoria.Categoria.CIÊNCIA):
                    while __x < len(estante.returnLivro()):
                        lista.append(estante.getLivroIndex(__x).getAutor())                    
                        
        if(len(lista) == 0):
            print("Não há autores nesta lista")
        else:
            return lista

    def listarTudo(self):
        for estante in self.__estante:
            print("Estante:", estante.getNome())
            estante.returnLivro()

    def escolherCategoria(self):
        opt = input(print("Digite: 1 - Filosofia, 2 - Ciência, 3 - Literatura."))

        if(opt == '1'):
            return Categoria.Categoria.Filosofia,
        elif(opt == '2'):
            return Categoria.Categoria.Ciência,
        elif(opt == '3'):    
            return Categoria.Categoria.Literatura
        else:
            return "Categoria inválida!"
