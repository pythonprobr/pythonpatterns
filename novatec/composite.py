r"""
Exemplo do padão Composite
==========================

Aplicação: catálogo de produtos eletrônicos para hobistas.

A *Folha* de um catálogo é a classe ``Componente``::

    >>> ard = Componente(1, 'Arduino Uno', 79.95)
    >>> ard
    Componente(sku=1, nome='Arduino Uno', preco=79.95)
    >>> ard.preco
    79.95
    >>> bobs = Componente(2, "Bob's Duino", 59.95)
    >>> bobs
    Componente(sku=2, nome="Bob's Duino", preco=59.95)
    >>> str(ard)
    'Arduino Uno (#1)\t$79.95'
    >>> cabo_usb = Componente(3, 'Cabo USB azul 1m', 4.95)

Um catálogo é uma lista de produtos, que pode ser exibida formatada::

    >>> cat = Catalogo([ard, bobs, cabo_usb])
    >>> cat
    <Catalogo (3 produtos)>
    >>> print(cat)  # doctest: +NORMALIZE_WHITESPACE
    Arduino Uno (#1) $79.95
    Bob's Duino (#2) $59.95
    Cabo USB azul 1m (#3) $4.95

Um kit é um produto formato por mais de um componente.

    >>> kit1 = Kit(4, 'Arduino completíssimo', [ard, cabo_usb])
    >>> kit1
    <Kit #4 'Arduino completíssimo' (2 produtos)>

Por padrão, o preço do kit é soma dos preços dos componentes incluídos.

    >>> kit1.preco
    84.9

A apresentação do kit inclui o nome dos componentes::

    >>> print(kit1)  # doctest: +NORMALIZE_WHITESPACE
    Arduino completíssimo (#4) $84.90
    - Arduino Uno
    - Cabo USB azul 1m

Na listagem do catálogo, os componentes dos kits também aparecem::

    >>> cat = Catalogo([kit1, ard, bobs, cabo_usb])
    >>> print(cat)  # doctest: +NORMALIZE_WHITESPACE
    Arduino completíssimo (#4) $84.90
    - Arduino Uno
    - Cabo USB azul 1m
    Arduino Uno (#1) $79.95
    Bob's Duino (#2) $59.95
    Cabo USB azul 1m (#3) $4.95

"""

class Componente:
    """Classe *Folha* (*Leaf*) no design pattern"""

    def __init__(self, sku, nome, preco):
        self.sku = sku
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return "Componente(sku={}, nome={!r}, preco={})".format(
                    self.sku, self.nome, self.preco)

    def __str__(self):
        return '{} (#{})\t${}'.format(self.nome, self.sku, self.preco)


class Kit:
    """Classe *Composite* no design pattern"""

    def __init__(self, sku, nome, produtos):
        self.sku = sku
        self.nome = nome
        self.produtos = list(produtos)

    def __repr__(self):
        return '<Kit #{} {!r} ({} produtos)>'.format(
            self.sku, self.nome, len(self.produtos))

    def __str__(self):
        saida = ['{} (#{})\t${:0.2f}'.format(self.nome, self.sku, self.preco)]
        for produto in self.produtos:
            saida.append('- {}'.format(produto.nome))
        return '\n'.join(saida)


    @property
    def preco(self):
        return sum(p.preco for p in self.produtos)


class Catalogo:
    """Classe *Cliente* no design pattern"""

    def __init__(self, produtos):
        self.produtos = list(produtos)

    def __repr__(self):
        return '<Catalogo ({} produtos)>'.format(len(self.produtos))

    def __str__(self):
        saida = []
        for produto in self.produtos:
            saida.append(str(produto))
        return '\n'.join(saida)
