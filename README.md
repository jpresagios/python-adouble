# python-adouble
Algorithmic Diferentiation through Overloading on Python using the forward method

This a Tapeless implementation at this moment is only toy code to
review AD on Python using Overloading operator.

# Use
from ADouble import *

x1 = ADouble(5)
x2 = ADouble(10)


x1.independent()
x2.independent()

y = x1 + x2 * x1

print(y.val)
print(y.der)