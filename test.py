from ADouble import *

x1 = ADouble(5)
x2 = ADouble(10)


x1.independent()
x2.independent()

y = x1 + x2 * x1

print(y.val)
print(y.der)