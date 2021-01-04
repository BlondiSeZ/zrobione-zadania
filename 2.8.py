a = input("Podaj 1 sciane przy prostokątną")
b = input("Podaj 2 sciane przy prostokątną")
c = input("Podaj 3 sciane przeciwprostokątną")

a1 = float(a) * float(a)
b1 = float(b) * float(b)
c1 = float(c) * float(c)

if float(a1) + float(b1) == float(c1):
    print("Trójkąt jeest prostokątny")
else:
    print("Trójkąt nie jest prostokątny")