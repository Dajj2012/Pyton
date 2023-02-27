koll = int(input('Введите колличество монет '))
orel = 0
reshka = 0
for i in range(koll):
    x = int(input('Введите 1 если орел иначе 0 '))
    if x == 0:
        orel += 1
    else:
        reshka += 1
if reshka > orel:
    print(orel)
else:
    print(reshka)
