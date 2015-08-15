"""
    >>> t1 = Treco()
    >>> t2 = Treco()
    >>> t1 is t2
    False
    >>> s1 = Singleton()
    >>> s2 = Singleton()
    >>> s1 is s2
    True
    >>> id(s1), id(s2)

"""


class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_a_instancia'):
            cls._a_instancia = super().__new__(cls, *args, **kwargs)
        return cls._a_instancia


class Treco:
    pass
