s=int(input('Введите сумму чисел: '))
p=int(input('Введите произведение чисел: '))
discriminant= s**2-4*p
if discriminant<0:
    print("Чисел не существуют")
else:
    x1 = (s + discriminant**0.5) / 2
    x2 = (s - discriminant**0.5) / 2
    y1=s-x1
    y2=s-x2
    print(f'x1={int(x1)} y1={int(y1)}')
    print(f'x2={int(x2)} y2={int(y2)}')