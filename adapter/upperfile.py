"""
    >>> with UppercasingFile('teste.txt', 'wt', encoding='utf-8') as f:
    ...    f.write('Testando...')
    11
    >>> with UppercasingFile('teste.txt', encoding='utf-8') as f:
    ...    s = f.read()
    >>> s
    'TESTANDO...'

"""



class UppercasingFile:
    def __init__(self, *a, **k):
        self.f = open(*a, **k)

    def write(self, data):
        return self.f.write(data.upper())

    def __getattr__(self, name):
        return getattr(self.f, name)

    def __enter__(self, *a, **k):
        return self

    def __exit__(self, *a, **k):
        self.f.__exit__(*a, **k)


