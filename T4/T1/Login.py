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
        m = new Menu()
        x = []
        x = m.menu()
        if(x[0] in self.__admin and x[1] in admin):
			temp = Admin()
			return temp
		elif(x[0] in bibliotecario and x[1] in bibliotecario):
			temp = Bibliotecario()
			return temp
		elif(x[0] in guest and x[1] in guest):
			temp = Guest()
			return temp
		}
		return Null

    def CallMenu(self, x):
        if(x == Null):
            print("Fim")
        x.Login()