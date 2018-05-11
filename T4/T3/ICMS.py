from Imposto import Imposto

class ICMS(Imposto):
    def __init__(self):
        super().__init__(0.90)