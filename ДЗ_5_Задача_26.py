def qrt (a, b):
    if b==0:
        return 1
    if b==2:
        return a*a
    else:
        return qrt(a,b-1)*a


numberA = int(input('Введите  число '))
numberB = int(input('Введите  степень '))
print(qrt(numberA, numberB))
