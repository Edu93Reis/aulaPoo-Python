from Partido import Partido

class Candidato:
    def __init__(self, __nome, __nacionalidade, __partido):
        if(__nome is None):
            print("Candidato deve possuir nome!")
            __nome = str(input("Digite nome: "))
            self.__nome = __nome
        else:
            self.__nome = __nome
        
        if(__nacionalidade is None):
            print("Candidato deve possuir nacionalidade!")
            __nacionalidade = str(input("Digite nacionalidade: "))
            self.__nacionalidade = __nacionalidade
        else:
            self.__nacionalidade = __nacionalidade
        
        if(__partido.getNome() is None and __nacionalidade == "brasileiro"):
            print("Candidato deve possuir partido!")
            __nP = str(input("Digite nome partido: "))
            __ide = str(input("Digite ideologia do partido: "))
            __si = str(input("Digite sigla do partido: "))
            __num = int(input("Digite número do partido: "))

            __p = Partido(__nP, __ide, __si, __num)

            self.__partido = __p            
        else:    
            self.__partido = __partido

    def getNome(self):
        return self.__nome

    def getNacionalidade(self):
        return self.__nacionalidade

    def getPartido(self):
        return self.__partido

    def setPartido(self, __partido):
        self.partido = __partido