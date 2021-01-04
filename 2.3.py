a = input("Podaj liczbe pierwszą")
b = input("Podaj liczbe drugą")
c = input("Podaj liczbe trzecią")

if a > b and a > c and b > c:
    print("Największą liczbą jest liczba A: " + a)
    print("Drugą liczbą jest liczba B: " + b)
    print("Najmniejszą liczbą jest liczba C: " + c)
elif a > b and a > c and c > b:
    print("Największą liczbą jest liczba A: " + a)
    print("Drugą liczbą jest liczba C: " + c)
    print("Najmniejszcą liczbą jest liczba B: " + b)
elif b > a and b > c and a > c:
    print("Największą liczbą jest liczba B: " + b)
    print("Drugą liczbą jest liczba A: " + a)
    print("Najmniejszcą liczbą jest liczba C: " + c)
elif b > a and b > c and c > a:
    print("Największą liczbą jest liczba B: " + b)
    print("Drugą liczbą jest liczba C: " + c)
    print("Najmniejszcą liczbą jest liczba A: " + a)
elif c > a and c > b and a > b:
    print("Największą liczbą jest liczba C: " + c)
    print("Drugą liczbą jest liczba A: " + a)
    print("Najmniejszcą liczbą jest liczba B: " + b)
elif c > a and c > b and b > a:
    print("Największą liczbą jest liczba C: " + c)
    print("Drugą liczbą jest liczba A: " + b)
    print("Najmniejszcą liczbą jest liczba B: " + a)
elif a > b and b == c:
    print("Największą liczbą jest liczba A: " + a)
    print("Liczby B i C są równe i wynoszą: " + b)
elif b > a and a == c:
    print("Największą liczbą jest liczba B: " + b)
    print("Liczby A i C są równe i wynoszą: " + c)
elif b > a and a == c:
    print("Największą liczbą jest liczba B: " + b)
    print("Liczby A i C są równe i wynoszą: " + c)
elif c > b and b == a:
    print("Największą liczbą jest liczba C: " + c)
    print("Liczby B i C są równe i wynoszą: " + b)
elif a == b and b < a:
    print("Największymi liczbami są A i B i wynoszą: " + b)
    print("Najmniejszą liczbą jest C: " + c)
elif a == c and b < a:
    print("Największymi liczbami są A i C i wynoszą: " + c)
    print("Najmniejszą liczbą jest B: " + b)
elif c == b and a < c:
    print("Największymi liczbami są C i B i wynoszą: " + b)
    print("Najmniejszą liczbą jest A: " + a)