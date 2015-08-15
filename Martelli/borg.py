"""
    >>> b1 = Borg()
    >>> b2 = Borg()
    >>> b1 is b2
    False
    >>> b1.i_know_kung_fu = True
    >>> b2.i_know_kung_fu
    True
    >>> del b2.i_know_kung_fu
    >>> b1.i_know_kung_fu
    Traceback (most recent call last):
        ...
    AttributeError: 'Borg' object has no attribute 'i_know_kung_fu'
"""


class Borg:

    _estado_compartilhado = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._estado_compartilhado
        return obj
