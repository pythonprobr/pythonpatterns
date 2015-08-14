class EmbrulhoRestritor:

    def __init__(self, embrulhado, bloqueios):
        self._embrulhado = embrulhado
        self._bloqueios = bloqueios

    def __getattr__(self, nome):
        if nome in self._bloqueios:
            msg = 'atributo bloqueado: {!r}'.format(nome)
            raise AttributeError(msg)
        else:
            return getattr(self._embrulhado, nome)

    def exportar(self):
        return {'embrulhado': self._embrulhado,
                'bloqueios': self._bloqueios}


class Cao:

    def latir(self):
        print('Au!')

    def morder(self):
        print('Nhac!')
