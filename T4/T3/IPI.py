from Imposto import Imposto

class IPI(Imposto):

    def __init__(self):
        self._aliquota = _aliquota = 0.90
        super(IPI, self).__init__(_aliquota)