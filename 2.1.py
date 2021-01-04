a = input("Podaj liczbę pierwszą")
b = input("Podaj liczbę drugą")

c = int(a) % int(b)

if c == 0:
    print("Licza jest podzielna")
else:
    print("Liczba nie jest podzielna")