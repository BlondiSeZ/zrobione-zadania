i = input("podaj liczbę")
while int(i)!=0:
    o = input("podaj kolejną liczbę")
    sr = (int(i)+int(o))/2
    print(sr)
    break
else:
    print("zakończyłeś działanie pętli")