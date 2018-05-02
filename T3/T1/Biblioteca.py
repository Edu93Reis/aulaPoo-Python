from Estante import Estante
from Categoria import Categoria

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.estante = []

    def getNome(self):
        return self.nome

    def getEstante(self, i):
        if self.estante(i) in self.estante:
            return self.estante(i)

    def getEstante(self):
        return self.estante

    def inserirEstante(self, estante):
        if(self.estante is not Null):
            self.estante.append(estante)
        else:
            print("Entre com valor válido")

    def criarestante(self):
        nome = ""
        categoria = ""
        while(nome == "" or categoria == ""):
            input("Digite o nome da estante: ")
            input("Digite o categoria da estante: ")
            
            if(categoria == ""):
                print("Preencha a categoria: ")
            elif(nome == ""):
                print("Preencha o nome")
            else:
                print("Estante criada com sucesso")
    
    def listarfilosofia(self):
        novo = []
        for(estante in Estante):
            if(self.estante.getCategoria() == Categoria.Categoria.Filosofia):
                for(livro in Estante):
                    novo.append(estante).getLivro()
    return novo

    def contarCiencia(self):    
        cont = 0
        for(estante in Estante):
            if(estante.getCategoria() == Categoria.Categoria.Ciência):
                cont = cont+ self.estante.len(getLivro())
        return cont

    def listarAutores(self):
        lista = []
        for(estante in Estante):
            if(estante.getCategoria() == cat):
                for(livro in Livro):
                    lista.append(estante.livro.getAutor())
        if(len(lista) == 0):
            print "Não há autores nesta lista"
    return lista

    def listarTudo(self):
        for(estante in Estante):
            print("Estante:", estante.getNome())
            estante.getLivro()

    def escolherCategoria(self):
        opt = input(print("Digite: 1 - Filosofia, 2 - Ciência, 3 - Literatura."))

        return {
            '1' : Categoria.Categoria.Filosofia,
            '2' : Categoria.Categoria.Ciência,
            '3' : Categoria.Categoria.Literatura
        }.get(x, null)
