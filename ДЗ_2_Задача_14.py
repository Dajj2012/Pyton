number=int(input('Введите число: '))
index=0
while 2**index<number:
    print(f'2^{index}={2**index}')
    index+=1