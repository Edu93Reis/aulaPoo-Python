from Pessoa import Pessoa

class Churrasco:

	def __init__(self, qtCarne, contador):
		self.qtCarne = qtCarne
		self.contador = contador

	def verificarConsumo(self):
        if (Pessoa.idade <= 3 or Pessoa.vegetariana == True):
	        self.qtCarne += 0
		elif (Pessoa.idade > 3 and Pessoa.idade <= 12):
			self.qtCarne += 1
		else:
			self.qtCarne += 2

		self.contador += 1

    def mediaConsumo(self, c, i):
		self.media = self.c / self.i
		print ("A media de kg de carne por pessoa é: ", self.media, " kgs")

	def totalConsumo(self):
		print ("O total de kg de carne por pessoa é: ", self.qtCarne, " kgs")
