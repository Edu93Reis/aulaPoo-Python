class Partido:
    def __init__(self, __nome, __ideologia, __sigla, __num):
        self.__nome = __nome
        self.__ideologia = __ideologia
        self.__sigla = __sigla
        self.__num = __num

    def getNome(self):
        return self.__nome

    def getIdeologia(self):
        return self.__ideologia

    def getSigla(self):
        return self.__sigla

    def getNum(self):
        return self.__num

        