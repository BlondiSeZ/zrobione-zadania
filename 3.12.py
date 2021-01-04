import random
tries = 0
while tries < 50:
    tries += 1
    coin = random.randint(0, 1)
    if coin == 0:
        print('orzeł')
    if coin == 1:
        print ('reszka')
total = tries
print(total)