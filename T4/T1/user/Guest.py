from User import User
from biblioteca.MenuGuest import MenuGuest

class Guest(User):
    def __init__(self):
        super(self).__init__

    def Login(self):
        m = MenuGuest()
        m.menu()
