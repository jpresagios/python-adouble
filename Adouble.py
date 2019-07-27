class ADouble(object):
    """
    An Adouble instance store a variable value and its derivatives. The basic 
    arithmethic operations are overloaded so they propagate the
    values of the derivatives as well as the direct computation.
    """
    def __init__(self, value = 1, derivate = 0):
        self.val = float(value)
        self.der = float(derivate)