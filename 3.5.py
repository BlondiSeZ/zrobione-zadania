i = int(input("wpisz liczbe ktorej silnie chcesz znalezc:"))

silnia = 1

for x in range(1, i + 1):
    silnia = silnia * x
print("silnia", i, "=", silnia)
