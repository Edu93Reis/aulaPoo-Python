from user.User import User
from Biblioteca.Menu import Menu

class Guest(User):
    def __init__(self):
        super(self).__init__

    def Login(self):
        MenuGuest m = MenuGuest()
        m.menu()
