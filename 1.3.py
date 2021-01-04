h = int(86400)
d = int(24)
s = int(1)
m = int(60)
import datetime

teraz = datetime.datetime.now()
print('Czas systemu operacyjnego: ', teraz)

dzien = str(teraz.day)
print('Dzień: ', teraz.day)

sekunda = str(teraz.second)
print('Sekunda: ', sekunda)


h = s * 60 * 60
r = s * 60 * 60 * 24 * 365
z = s * 60 * 60 * 24 * 12

print(h)
print(r)