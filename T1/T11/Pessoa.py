class Pessoa():
    def __init__(self, nome, sexo, idade, vegetariana):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.vegetariana = vegetariana
    
    def getIdade(self):
        return self.idade

    def getVegetariano(self):
        return self.vegetariana


