from Partidos import Partidos
from Partido import Partido
from Candidato import Candidato

class Eleicao:
    p1 = Partido(Partidos.Nome.PT.value, Partidos.Ideologia.PT.value, Partidos.Sigla.PT.value, Partidos.Numero.PT.value)
    p2 = Partido(Partidos.Nome.PTB.value, Partidos.Ideologia.PTB.value, Partidos.Sigla.PTB.value, Partidos.Numero.PTB.value)
    p3 = Partido(Partidos.Nome.PSOL.value, Partidos.Ideologia.PSOL.value, Partidos.Sigla.PSOL.value, Partidos.Numero.PSOL.value)
    p4 = Partido(Partidos.Nome.PSDB.value, Partidos.Ideologia.PSDB.value, Partidos.Sigla.PSDB.value, Partidos.Numero.PSDB.value)
    c1 = Candidato("Lula", "Brasileiro", p1)
    c2 = Candidato("José Serra", "Americano", p2)
    c3 = Candidato("Tiririca", "Grego", p3)

    print("Candidato:", c1.getNome(),"de nacionalidade",c1.getNacionalidade(),"está no partido:", c1.getPartido().getNome(), 
    "de número:",c1.getPartido().getNum(),", sigla", c1.getPartido().getSigla() ,"e ideologia", c1.getPartido().getIdeologia())
    c1.setPartido(p3)
    print("Candidato:",c1.getNome(),"de nacionalidade",c1.getNacionalidade(),"está no partido:",c1.getPartido().getNome(), 
    "de número:",c1.getPartido().getNum(),", sigla", c1.getPartido().getSigla(),"e ideologia", c1.getPartido().getIdeologia())
    c1.setPartido(p4)
    print("Candidato:",c1.getNome(),"de nacionalidade",c1.getNacionalidade(),"está no partido:",c1.getPartido().getNome(), 
    "de número:",c1.getPartido().getNum(),", sigla",c1.getPartido().getSigla() ,"e ideologia", c1.getPartido().getIdeologia())
    print("Candidato:",c2.getNome(),"de nacionalidade", c2.getNacionalidade(),"está no partido:",c2.getPartido().getNome(), 
    "de número:",c1.getPartido().getNum(),", sigla",c1.getPartido().getSigla(),"e ideologia", c1.getPartido().getIdeologia())
    c3.setPartido(p2)
    print("Candidato:",c3.getNome(),"de nacionalidade",c3.getNacionalidade(),"está no partido:",c3.getPartido().getNome(),
    "de número:",c1.getPartido().getNum(),", sigla",c1.getPartido().getSigla() ,"e ideologia", c1.getPartido().getIdeologia())