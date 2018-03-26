from Bateria import Bateria

class Celular:
    __identificador = 0

    def __init__ (self, __nomeUser, __bateria):
        #identificador é um elemento estático e precisa do nome da classe antes do elemento para funcionar
        Celular.__identificador += 1 
        self.__nomeUser = __nomeUser
        self.__bateria = __bateria
        self.__ligado = False
    
    def getId(self):
        return self.__identificador

    def getUser(self):
        return self.__nomeUser

    def setBateria(self, __bateria):
        if(self.__ligado == True):
            self.__ligado = False
        
        self.__bateria = __bateria
    
    def ligaCelular(self):
        if(self.__ligado == False):
            if(self.__bateria.getCarga()>20):
                self.__ligado = True
                print("Usuário: ", self.getUser(), ", ID Celular: ", self.getId())
            elif(self.__bateria.getCarga() == 0):
                pass
            else:
                self.__ligado = True
                self.__bateria.getCarga()
        else:
            print("Celular já está ligado!")

    def desligaCelular(self):
        if(self.__ligado == True):
            if(self.__bateria.getCarga()>=20):
                self.__ligado = False
            else:
                print("Bye!")
                if(self.__bateria.getCarga()>20):
                    self.__bateria.setCarga(self.__bateria.setCarga()-10)
                    self.__ligado = False
        else:
            self.__ligado = False

    def tocaSom(self):
        if(self.__ligado == True):
            if(self.__bateria.getCarga()>10):
                print("Baaat-maaan!!")