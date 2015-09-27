
class Borg:
    _estado_compartilhado = {}

    def __new__(cls, *args, **kwargs):
        novo_borg = super().__new__(cls, *args, **kwargs)
        novo_borg.__dict__ = cls._estado_compartilhado
        return novo_borg
