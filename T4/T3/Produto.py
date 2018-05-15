from Imposto import Imposto

class Produto:

    def __init__(self,__nome,__preco,__imposto):
        self.__nome = __nome
        self.__preco = __preco
        self.__imposto = __imposto

    def getPreco(self):
        return self.__preco * self.__imposto.getAliquota()

    def getNome(self):
        return self.__nome

    def setImposto(self, __imposto):
        self.__imposto = __imposto

    def getProduto(self):
        print("Nome: ",self.getNome()," Preco: ",self.getPreco())