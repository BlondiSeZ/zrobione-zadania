a = input("Podaj zmienną")

if float(a) < 10:
    print("Wartość jest mniejsza bądź równa 10")
elif float(a) == 10:
    print("Wartość jest mniejsza bądź równa 10")
elif float(a) > 10 and float(a) <= 25:
    print("Wartość jest większa od 10 i mniejsza bądź równa od 25")
elif float(a) > 25:
    print("Wartość jest wieksza od 25")
else:
    print("Wartość nieokreślona")