tel = {}
for i in range(10):
    nazwisko = str(input("Podaj nazwisko: "))
    numer = str(input("Podaj numer: "))
    tel[nazwisko] = numer
print(tel)
telf = list(tel.keys())[0]
tell = list(tel.keys())[len(tel)-1]
print(telf, tell)
tel[telf] = "b"
tel[tell] = "c"
print(tel)