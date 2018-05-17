from Estante import Estante
from Livro import Livro
from Categoria import Categoria

class Biblioteca:
    
    def __init__(self, __nome):
        __estante = []
        self.__nome = __nome
        self.__estante = __estante

    def getNome(self):
        return self.__nome

    def getEstante(self, i):
        if(self.__estante(i) in self.__estante):
            return self.__estante(i)

    def getEstantes(self):
        return self.__estante

    def inserirEstante(self, __estante):
        if(self.__estante is not None):
            self.__estante.append(__estante)
        else:
            print("Entre com valor válido")

    def criarEstante(self):
        __nome = ""
        __categoria = ""
        while(__nome == "" or __categoria == ""):
            __nome = input("Digite o nome da estante: ")
            __categoria = input("Digite o categoria da estante: ")
            
            if(__categoria == ""):
                print("Preencha a categoria: ")
            elif(__nome == ""):
                print("Preencha o nome")
            else:
                __e = Estante(__nome, __categoria)
                self.inserirEstante(__e)
                print("Estante criada com sucesso")
    
    def listarfilosofia(self):
        __novo = []
        for estante in self.__estante:
            if(estante.getCategoria() == Categoria.Categoria.Filosofia):
                for livro in self.__estante:
                   __novo.append(estante).livro.getLivro()
                    #novo.append(estante).getLivro()
        return __novo

    def contarCiencia(self):    
        __cont = 0
        for estante in self.__estante:
            if(estante.getCategoria() == Categoria.Categoria.Ciência):
                __cont = __cont + self.__estante.len(estante.getLivro())
        return __cont

    def listarAutores(self):
        lista = []
        for estante in self.__estante:
            if(estante.getCategoria() == Categoria.Categoria.CIÊNCIA):
                for livro in self.__livro:
                    lista.append(estante.livro.getAutor())
        if(len(lista) == 0):
            print("Não há autores nesta lista")
        return lista

    def listarTudo(self):
        for estante in self.__estante:
            print("Estante:", estante.getNome())
            estante.getLivro()

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
