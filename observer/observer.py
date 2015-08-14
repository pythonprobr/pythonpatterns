"""
    >>> WriteEvent.register(log)
    >>> WriteEvent.notify('file #1')
    file #1 was written
    >>> WriteEvent.register(AnotherObserver())
    >>> WriteEvent.notify('file #2')
    file #2 was written
    Yeah WriteEvent told me!

"""


class Event(object):
    _observers = []

    def __init__(self, subject):
        self.subject = subject

    @classmethod
    def register(cls, observer):
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def unregister(cls, observer):
        if observer in cls._observers:
            self._observers.remove(observer)

    @classmethod
    def notify(cls, subject):
        event = cls(subject)
        for observer in cls._observers:
            observer(event)

class WriteEvent(Event):

    def __repr__(self):
        return 'WriteEvent'

def log(event):
    print('%s was written' % event.subject)


class AnotherObserver(object):
    def __call__(self, event):
        print('Yeah %s told me!' % event)

if __name__ == '__main__':
    import doctest
    failed, attempted = doctest.testmod()
    if not failed:
        print('OK: %s tests passed' % attempted)
    else:
        print('FAIL: %s test(s) failed (of %s total)'
              % (failed, attempted))
