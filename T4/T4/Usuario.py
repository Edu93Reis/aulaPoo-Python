class Usuario:
    def __init__ (self, _login):
        self._login = _login

    def boasVindas(self):
        print("Bem-vindo,", self._login)

    def descreve(self, datatype, args):
        if(datatype == 'Usuario'):
            print("Bem Vindo: "+ self._login)
        else:
            pass
    
    def despedida(self, datatype, usuario):
        if(datatype == 'Usuario'):
            usuario.despedida()
        else:
            pass