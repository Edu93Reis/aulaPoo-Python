from User import User
from biblioteca.MenuBibliotecario import MenuBibliotecario

class Bibliotecario(User):
    def __init__(self):
        super(self).__init__

    def Login(self):
        m = MenuBibliotecario()
        m.menu()
