
# EAFP -> It's Easier to Ask Forgiveness than Permission
def docmd(self, cmd, a):
    #...
    try:
        fn = getattr(self, 'do_' + cmd)
    except AttributeError:
        return self.dodefault(cmd, a)
    return fn(a)


def docmd(self, cmd, a):
    #...
    return getattr(self, 'do_' + cmd, self.dodefault)(a)


# LBYL -> Look Before You Leap
def docmd(self, cmd, a):
    #...
    if hasattr(self, 'do_' + cmd):
        fn = getattr(self, 'do_' + cmd)
        return fn(a)
    else:
        return self.dodefault(cmd, a)
