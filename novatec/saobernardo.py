
class Barril:

    def __init__(self, doses=10):
        self.doses = doses

    def servir(self):
        if self.doses > 0:
            return '1 dose'
        else:
            raise LookupError('barril vazio')

    def encher(self, doses):
        self.doses += doses

class SaoBernardo:

    def __init__(self, nome):
        self.nome = nome
        self._barril = Barril()

    def servir(self):
        dose = self._barril.servir()
        print('{} servindo: {}'.format(self.nome, dose))
        return dose

    def __getattr__(self, nome):
        if hasattr(self._barril, nome):
            return getattr(self._barril, nome)
        else:
            raise AttributeError('atributo desconhecido')
