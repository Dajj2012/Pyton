list1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
list2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
list3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
list4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
list5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
list8 = ['J', 'X', 'Ш', 'Э', 'Ю']
list10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
slovo = str(input('Введите слово '))
index_slovo = 0
summ = 0
for i in range(len(slovo)):
    flag = 0
    for item in list1:
        if item == slovo[i]:
            summ += 1
            flag = 1
            break
    if flag == 0:
        for item in list2:
            if item == slovo[i]:
                summ += 2
                flag = 1
                break
    if flag == 0:
        for item in list3:
            if item == slovo[i]:
                summ += 3
                flag = 1
                break
    if flag == 0:
        for item in list4:
            if item == slovo[i]:
                summ += 4
                flag = 1
                break
    if flag == 0:
        for item in list5:
            if item == slovo[i]:
                summ += 5
                flag = 1
                break
    if flag == 0:
        for item in list8:
            if item == slovo[i]:
                summ += 8
                flag = 1
                break
    if flag == 0:
        for item in list10:
            if item == slovo[i]:
                summ += 10
                break
print(summ)



