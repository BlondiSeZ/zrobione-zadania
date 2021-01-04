tup1 = ("szafka", "szczotka", "biurko", "okno", "lampa", "lozko")
for i in tup1:
    s = str(input("Podaj słowo: "))
    if s in tup1:
        print("Szukane słowo jest w krotce")
        print("Jego indeks: ", tup1.index(s))
        break
    else:
        print("Nie ma takiego słowa.")
        break
tup2 = tup1 + ("garnek", "patelnia", "zlew", "lodowka", "przyprawy", "kosz")
for i in tup2:
    s = str(input("Podaj kolejne słowo: "))
    if s in tup2:
        print("Szukane słowo też jest w krotce")
        print("Jego indeks: ", tup2.index(s))
        break
    else:
        print("Wciąż nie ma takiego słowa.")
        break