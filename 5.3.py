a = list(input("Podaj ciąg liczb: "))
tab_r = a[::-1]
# print(a)
# print(tab_r)
if tab_r == a:
    print("Palindrom, a to rezultat: ", tab_r)
else:
    print("Odwrócona: ", tab_r)