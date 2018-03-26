from Partido import Partido

class Candidato:
    def __init__(self, __nome, __nacionalidade, __partido):
        self.__nome = __nome
        self.__nacionalidade = __nacionalidade
        self.__partido = __partido

    def getNome(self):
        return self.__nome

    def getNacionalidade(self):
        return self.__nacionalidade

    def getPartido(self):
        return self.__partido

    def setPartido(self, __partido):
        self.__partido = __partido