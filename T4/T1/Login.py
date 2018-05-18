from user.Admin import Admin
from user.Bibliotecario import Bibliotecario
from user.Guest import Guest
from user.User import User
from Menu import Menu

class Login:
    def __init__(self):
        self.__admin = "admin"
        self.__guest = "guest"
        self.__bibliotecario = "bibliotecario"

    def Validation(self):
        m = Menu()
        x = []
        x = m.menu()
        if(x[0] in self.__admin and x[1] in self.__admin):
            temp = Admin()
            return temp
        elif(x[0] in self.__bibliotecario and x[1] in self.__bibliotecario):
            temp = Bibliotecario()
            return temp
        elif(x[0] in self.__guest and x[1] in self.__guest):
            temp = Guest()
            return temp
            
        return None

    def CallMenu(self, x):
        if(x == None):
            print("Fim")
        x.Login()