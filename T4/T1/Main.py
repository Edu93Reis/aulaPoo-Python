from user.Admin import Admin
from user.Bibliotecario import Bibliotecario
from user.Guest import Guest
from user.User import User
from Menu import Menu
from Login import Login

class Teste:
    l = Login()
    while true:
        try:
            l.CallMenu(l.Validation())
        except ValueError:
            print("Login Inválido")

Teste()
