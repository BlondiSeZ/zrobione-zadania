max = int(input("wpisz wartosc najwieksza:"))
min = int(input("wpisz wartosc najmniejsza:"))
for i in range(min, max+1):
   if((i%6==0) & (i%9==0)):
      print(i)