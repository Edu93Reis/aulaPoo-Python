from User import User
from biblioteca.MenuAdmin import MenuAdmin

class Admin(User):
    def __init__(self):
        super(self).__init__

    def Login(self):
        m = MenuAdmin()
        m.menu()
