from Partido import Partido
from Candidato import Candidato

class Eleicao:
    p1 = Partido("Partido dos Trabalhadores", "Blabla" ,"PT", 13)
    p2 = Partido("Partido Socialista do Brasil", "Blabla", "PSB", 40)
    p3 = Partido("Partido Socialismo e Liberdade", "bla", "PSOL", 50)
    p4 = Partido("", "Nenhuma", "BLA", 14)
    c1 = Candidato("Marcelinho", "Brasileiro", p1)
    c2 = Candidato("Ronaldo", "Americano", p2)
    c3 = Candidato("", "Grego", p3)

    print("Candidato: ", c1.getNome(), " de nacionalidade ", c1.getNacionalidade()," está no partido ", c1.getPartido().getNome())
    c1.setPartido(p3)
    print("Candidato: ",c1.getNome()," de nacionalidade ",c1.getNacionalidade()," está no partido ",c1.getPartido().getNome());
    c1.setPartido(p4);
    print("Candidato: ", c1.getNome()," de nacionalidade ",c1.getNacionalidade()," está no partido ",c1.getPartido().getNome());
    print("Candidato: ", c2.getNome(), " de nacionalidade ", c2.getNacionalidade()," está no partido ",c2.getPartido().getNome());
    c3.setPartido(p2);
    print("Candidato: ",c3.getNome()," de nacionalidade ",c3.getNacionalidade()," está no partido ",c3.getPartido().getNome());