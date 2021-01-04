a = input("Podaj pierwszą liczbę")
b = input("Podaj drugą liczbę")
c = input("Podaj trzecią liczbę")
d = input("Podaj czwartą liczbę")

if a > b and a > c and a > d:
    print("A jest największą liczbą: " + a)
elif b > a and b > c and b > d:
    print("B jest największą liczbą: " + b)
elif c > a and c > b and c > d:
    print("C jest największą liczbą: " + c)
elif d > a and d > c and d > b:
    print("D jest największą liczbą: " + d)