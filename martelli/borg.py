class Borg:

    _estado_compartilhado = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._estado_compartilhado
        return obj
