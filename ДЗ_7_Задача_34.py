def glasnie (list: str):
    summ = 0
    for i in range(len(list)):
        if list[i] in 'аеёиоуыэюя':
            summ += 1
    return summ

fraza = input('введите фразу ')
spisok_slov = fraza.split()
flag = 0
for i in range(1, len(spisok_slov)):
    if glasnie(spisok_slov[i-1]) != glasnie(spisok_slov[i]):
        flag = 1
if flag == 0:
    print('Парам пам-пам')
else:
    print('Пам парам')