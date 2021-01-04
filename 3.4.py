max = int(201)
min = int(100)

for i in range(min, max):

    if((i%2!=0) & (i%5!=0) & (i%6!=0) & (i%11!=0)):
        print(i)