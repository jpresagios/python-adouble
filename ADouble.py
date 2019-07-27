def add(x, y):
    """
    x: Adouble instance
    y: Adouble instance
    """
    return ADouble(x.val + y.val, x.der + y.der)

def sub(x, y):
    """
    x: Adouble instance
    y: Adouble instance
    """
    return ADouble(x.val - y.val, x.der - y.der)

def mult(x, y):
    """
    x: Adouble instance
    y: Adouble instance
    """
    return ADouble(x.val * y.val, x.der * y.val + x.val * y.der)

def div(x, y):
    """
    x: Adouble instance
    y: Adouble instance
    """
    return ADouble(x.val / y.val, (x.der - y.der) / (y.val * y.val))


class ADouble(object):
    """
    An Adouble instance store a variable value and its derivatives. The basic 
    arithmethic operations are overloaded so they propagate the
    values of the derivatives as well as the direct computation.
    """
    def __init__(self, value = 1, derivate = 0):
        self.val = float(value)
        self.der = float(derivate)

    def independent(self):
        self.der = 1
        
    def __add__(self, y):
        if type(y) == type(self):
            return add(self, y)
        else:
            y = ADouble(y,0)
            return self + y

    def __radd__(self, y):
        if type(y) == type(self):
            return add(y, self)
        else:
            y = ADouble(y,0)
            return y + self


    def __sub__(self, y):
        if type(y) == type(self):
            return sub(self, y)
        else:
            y = ADouble(y,0)
            return self - y

    def __rsub__(self, y):
        if type(y) == type(self):
            return sub(y, self)
        else:
            y = ADouble(y, 0)
            return y - self


    def __mul__(self, y):
        if type(y) == type(self):
            return mult(self, y)
        else:
            y = ADouble(y, 0)
            return self * y

    def __rmul__(self, y):
        if type(y) == type(self):
            return mult(y, self)
        else:
            y = ADouble(y,0)
            return y * self

    
    def __div__(self, y):
        if type(y) == type(self):
            return div(self, y)
        else:
            y = ADouble(y,0)
            return self / y

    def __rdiv__(self, y):
        if type(y) == type(self):
            return div(y, self)
        else:
            y = ADouble(y,0)
            return y / self