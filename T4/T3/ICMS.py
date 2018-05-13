from Imposto import Imposto

class ICMS(Imposto):
    def __init__(self):
        self._aliquota = _aliquota = 0.90
        super(ICMS, self).__init__(_aliquota)