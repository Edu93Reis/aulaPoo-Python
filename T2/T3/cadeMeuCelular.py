from Celular import Celular
from Bateria import Bateria

class Teste():
    b1 = Bateria(70)
    print(b1.Carrega())
    print(b1.Carrega())
    print(b1.Carrega())
    print(b1.Descarrega())
    print(b1.Descarrega())
    c1 = Celular("Eduardo", b1)
    c1.ligaCelular()
    c1.tocaSom()
    c1.desligaCelular()
    c1.ligaCelular()
    c1.ligaCelular()
    c1.desligaCelular()
    print("Carga final: ",b1.getCarga())

    b2 = Bateria(23)
    c1.setBateria(b2)
    c1.ligaCelular()
    c1.tocaSom()
    print(b2.getCarga())
    c2 = Celular("Caio", b1)
    c2.ligaCelular()