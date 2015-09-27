"""
Um trem é um iterável com vagões.

O construtor pede o número de vagões::

    >>> t = Trem(3)

O trem é um iterável::

    >>> it = iter(t)

E o iterador obtido devolve vagões::

    >>> next(it)
    'vagão #1'
    >>> next(it)
    'vagão #2'
    >>> next(it)
    'vagão #3'

Somente a quantidade correta de vagões é devolvida::

    >>> next(it)
    Traceback (most recent call last):
      ...
    StopIteration

Finalmente, podemos percorrer um trem num laço ``for``::

    >>> for vagao in Trem(3):
    ...     print(vagao)
    ...
    vagão #1
    vagão #2
    vagão #3


"""

class Trem:

    def __init__(self, qt_vagoes):
        self.qt_vagoes = qt_vagoes

    def __iter__(self):
        for i in range(self.qt_vagoes):
            yield 'vagão #{}'.format(i + 1)
