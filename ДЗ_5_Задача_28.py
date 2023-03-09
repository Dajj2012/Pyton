def summ(a, b):
    if b > 0:
        summ(a+1, b-1)
    if b == 0:
        print(f'Сумма чисел равна {a}')
        # return a

numberB = int(input('Введите  число '))
numberA = int(input('Введите  число '))
summ(numberA, numberB)
