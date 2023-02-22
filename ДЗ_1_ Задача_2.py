summa=int(input('Введите колличество изготовленых фигур детьми: '))
if summa%6==0:
    sergey= int(summa/6)
    petr= int(summa/6)
    kate=int(summa*4/6)
    print(f'Сергей сделал {petr} Катя сделала {kate}  Петр сделал {petr}')
else:
    print("Такое не возможно математически")