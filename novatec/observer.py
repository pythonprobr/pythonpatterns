"""

    >>> p = PesquisaEleitoral()
    >>> p.adicionar_votos('A', 5)
    5 votos adicionados para 'A'
    >>> p.adicionar_votos('B', 3)
    3 votos adicionados para 'B'

Observadores em ação::

    >>> p.vincular_observador(estatistica)
    >>> p.adicionar_votos('A', 2)
    2 votos adicionados para 'A'
    Estatística: A 70%, B 30%
    >>> p.vincular_observador(grafico)
    >>> p.adicionar_votos('B', 7)
    7 votos adicionados para 'B'
    Estatística: A 41%, B 59%
    A ############################
    B #########################################
"""

class PesquisaEleitoral:
    """Classe *Sujeito* do padrão *Observer*"""

    def __init__(self):
        self.votos = {'A':0, 'B':0}
        self.observadores = []

    def adicionar_votos(self, candidato, votos):
        print('{} votos adicionados para {!r}'.format(votos, candidato))
        self.votos[candidato] += votos
        self.notificar_observadores()

    def vincular_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self):
        for obs in self.observadores:
            obs(self)

def estatistica(pesquisa):
    total = sum(pesquisa.votos.values())
    pct_a = pesquisa.votos['A'] / total * 100
    pct_b = pesquisa.votos['B'] / total * 100
    print('Estatística: A {:0.0f}%, B {:0.0f}%'.format(pct_a, pct_b))

def grafico(pesquisa):
    total = sum(pesquisa.votos.values())
    print('A', '#' * int(pesquisa.votos['A'] / total * 70))
    print('B', '#' * int(pesquisa.votos['B'] / total * 70))
