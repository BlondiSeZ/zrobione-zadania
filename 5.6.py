import random
num = random.randint(1, 100)
for i in range(0,4):
    if i <3:
        x = int(input("Zgaduj liczbe"))
        if x > num:
            print("podałeś za duza wartosc")
        elif x < num:
            print("podalesz za mala wartosc")
        else:
            print("Zgadles!")
            break
    else:
        print("Haha przegrales!")