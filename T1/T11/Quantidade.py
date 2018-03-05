from Pessoa import Pessoa
from Churrasco import Churrasco

def Quantidade():

    p1 = Pessoa("Carlos", 25, "Masculino", True)
    p2 = Pessoa("João", 15, "Masculino", False)
    
    print("Nome: ", p1.nome,"/Idade: ", p1.idade,"/Sexo: ",p1.sexo,"/Vegetariana: ",p1.vegetariana)
    print("Nome: ", p2.nome,"/Idade: ", p2.idade,"/Sexo: ",p2.sexo,"/Vegetariana: ",p2.vegetariana)
    
    c1 = Churrasco(0, 0)
    c1.verificarConsumo(p1)
    c1.verificarConsumo(p2)

    c1.mediaConsumo(c1.contador, c1.qtCarne)
    c1.totalConsumo()

Quantidade()