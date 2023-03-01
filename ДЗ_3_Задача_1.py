import random
max_numer_in_list=100
list =[random.randint(0,max_numer_in_list) for _ in range(10)]
print(list)
flag=0
difference_min=max_numer_in_list+1
number = int(input('Введите искомое число '))
for i in range(len(list)):
    if list[i] == number:
        flag+=1
    else:
        difference=list[i]-number
        if difference<0:
            difference*=-1
        if difference<difference_min:
            difference_min=difference
            difference_min_index=i

if flag >0:
    print(f' число встречалось {flag} раз')
else:
    print(f' максимально близкое число {list[difference_min_index]}')