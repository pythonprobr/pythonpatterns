
class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_a_instancia'):
            cls._a_instancia = super().__new__(cls, *args, **kwargs)
        return cls._a_instancia

