from Pessoa import Pessoa
from Churrasco import Churrasco

def Quantidade():
    p1 = Pessoa("Carlos", "Masculino",25, True)
    p2 = Pessoa("João","Masculino",15, False)
    c1 = Churrasco()
    c1.verificarConsumo(p1)
    c1.verificarConsumo(p2)
    c1.totalConsumo()
    c1.mediaConsumo(c1.qtCarne, c1.contador)

Quantidade()