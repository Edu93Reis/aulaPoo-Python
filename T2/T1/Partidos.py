from enum import Enum

class Partidos(object):
    class Sigla(Enum):
        PT = "PT"
        PSOL = "PSOL"
        PSDB = "PSDB"
        PTB = "PTB"

    class Nome(Enum):
        PT = "Partido dos Trabalhadores"
        PSOL = "Partido Socialismo e Liberdade"
        PSDB = "Partido da Social Democracia Brasileira"
        PTB = "Partido Trabalhista Brasileiro"

    class Ideologia(Enum):
        PT = "Bla"
        PSOL = "Eita!"
        PSDB = "Blabla"
        PTB = "Vish"

    class Numero(Enum):
        PT = 13
        PSOL = 50
        PSDB = 45
        PTB = 14   