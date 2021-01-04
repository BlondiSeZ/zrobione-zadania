import math

a = input("Podaj wartoś A")
b = input("Podaj wartoś B")
c = input("Podaj wartoś C")

delta = (float(b) * float(b)) - 4 * float(a) * float(c)

x1 = ((-1 * float(b)) - math.sqrt(delta)) / (2 * float(a))
x2 = ((-1 * float(b)) + math.sqrt(delta)) / (2 * float(a))
print(x1)
print(x2)