a = input("Podaj liczbe")

b = int(a) % 2

if int(a) > 0:
    print("Liczba jest dodatnia")
    if b == 0:
        print("Liczba nie jest podzielna przez 2 z resztą")
    else:
        print("Liczba jest podzielna przez 2 z resztą")
elif int(a) < 0:
    print("Liczba jest ujemna")
    if b == 0:
        print("Liczba nie jest podzielna przez 2 z resztą")
    else:
        print("Liczba jest podzielna przez 2 z resztą")
else:
    print("Wpisałeś ZERO")
