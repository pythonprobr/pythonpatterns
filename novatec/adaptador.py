
"""

    >>> p = Parede()
    >>> f = Fonte(p)
    >>> a = Aparelho(f)
    >>> a.ligar()
    >>> a.ligado
    True

"""

class Aparelho:

    def __init__(self, fonte=None):
        self.fonte = fonte
        self.ligado = False

    def ligar(self):
        if self.fonte.corrente_continua():
            self.ligado = True

class Parede:

    def corrente_alternada(self):
        return True

class Fonte:

    def __init__(self, parede):
        self.parede = parede

    def converter(self):
        return self.parede.corrente_alternada()

    def corrente_continua(self):
        return self.converter()
