"""
Tômbola é uma estrutura que permite a retirada de itens de uma lista em
ordem aleatória sem repetição.

A tômbola é criada passando um iterável de itens::

    >>> colecao = 'ABCD'
    >>> t = Tombola(colecao)

A tômbola pode começar vazia::

    >>> t0 = Tombola()

Para saber se a tômbola está carregada, existe um método::

    >>> t.carregada()
    True
    >>> t0.carregada()
    False

Os itens são retirados um a um::

    >>> item = t.retirar()
    >>> item in colecao
    True

Uma vez sorteado, o item é retirado e quando todos são retirados
a tômbola fica vazia::

    >>> for i in range(3):
    ...     _ = t.retirar()
    ...
    >>> t.carregada()
    False

Se os itens forem misturados, espera-se que não sejam retirados na mesma
ordem em que foram colocados (de acordo com as proabilidades)::

    >>> qt_itens = 20
    >>> t = Tombola(range(qt_itens))
    >>> t.misturar()
    >>> retirados = []
    >>> for i in range(qt_itens):
    ...     retirados.append(t.retirar())
    ...
    >>> retirados != list(range(qt_itens))
    True

Para a conveniência do usuário, a instância de Tômbola pode ser invocada diretamente
para retirar um item::

    >>> um_a_tres = [1, 2, 3]
    >>> t = Tombola(um_a_tres)
    >>> sorteado = t()
    >>> sorteado in um_a_tres
    True




"""

from random import shuffle

class Tombola:
    """Armazena e devolve itens sorteados sem repetir"""

    def __init__(self, itens=None):
        if itens is None:
            self.itens = []
        else:
            self.itens = list(itens)

    def carregada(self):
        return bool(self.itens)

    def retirar(self):
        return self.itens.pop()

    def misturar(self):
        shuffle(self.itens)

    def __call__(self):
        return self.retirar()
        
