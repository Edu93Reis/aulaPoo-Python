class Churrasco:
    qtCarne = 0
    contador = 0

    def __init__(self):
        pass

    def verificarConsumo(self, pessoa):
        if (pessoa.idade <= 3):
            pass
        elif (pessoa.vegetariana == True):
            pass
        elif (pessoa.idade > 3) and (12 >= pessoa.idade):
            self.qtCarne = self.qtCarne + 1
        else:
            self.qtCarne = self.qtCarne + 2

        self.contador = self.contador + 1

    def totalConsumo(self):
        print("O total de kg de carne é: ", self.qtCarne, " kgs")

    def mediaConsumo(self, c, i):
        media = c / i
        print("A media de kg de carne por pessoa é: ", media, " kgs")