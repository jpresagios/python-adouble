# python-adouble
Algorithmic Diferentiation through Overloading on Python using the forward method

This a Tapeless implementation at this moment is only toy code to
review AD on Python using Overloading operator.

# Use
from ADouble import *<br>

x1 = ADouble(5)<br>
x2 = ADouble(10)<br>


x1.independent()<br>
x2.independent()<br>

y = x1 + x2 * x1<br>

print(y.val)<br>
print(y.der)<br>