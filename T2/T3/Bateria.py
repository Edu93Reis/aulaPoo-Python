class Bateria:
    __carga = 0

    def __init__(self,__carga):
        if((self.__carga<=100) and (self.__carga>=0)):
            self.__carga = __carga
        else:
            self.__carga = 100

    def getCarga(self):
        if(self.__carga>20):
            return self.__carga
        else:
            print("Bateria fraca!")
            return self.__carga

    def setCarga(self, __carga):
        if((self.__carga<=100) and (self.__carga>=0)):
            self.__carga = __carga
        else:
            self.__carga = __carga
    
    def Carrega(self):
        if(self.__carga<95):
            self.__carga += 5
        else:
            print("Bateria no limite, impossível aumentar a carga!!")
            self.__carga = 100
        
        return self.__carga
    
    def Descarrega(self):
        if(self.getCarga()>=10):
            self.__carga -=10
        else:
            self.__carga == 0

        return self.__carga
