potega = int(input("wpisz maksymalna potege:"))

result = list(map(lambda x: 2 ** x, range(potega)))

print("The total terms are:",potega)
for i in range(potega):
   print("2^",i,"=",result[i])