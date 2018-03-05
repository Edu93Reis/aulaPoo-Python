from Pessoa import Pessoa

class Churrasco:
	def __init__(self, Pessoa):
		self.pessoa = Pessoa
		self.qtCarne = 0
		self.contador = 0

	def verificarConsumo(self):		
        if ((Pessoa.getIdade <= 3) or (Pessoa.getVegetariano == True)):
	        self.qtCarne += 0
		elif ((Pessoa.getIdade > 3) and (Pessoa.getIdade <= 12)):
			self.qtCarne += 1
		else:
			self.qtCarne += 2

		self.contador += 1

	def mediaConsumo(self, qtCarne, contador):
		self.media = self.qtCarne / self.contador
		print ("A media de kg de carne por pessoa é: ", self.media, " kgs")

	def totalConsumo(self):
		print ("O total de kg de carne por pessoa é: ", self.qtCarne, " kgs")
