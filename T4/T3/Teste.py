from Imposto import Imposto
from IPI import IPI
from ICMS import ICMS
from Produto import Produto

def Teste():
    ipi = IPI()
    icms = ICMS()
    p1 = Produto("Carro",90640.00,ipi)
    p2 = Produto("Lego",120.00,icms)

    p1.getProduto()
    p1.setImposto(icms)
    p1.getProduto()
    p2.getProduto()

Teste()