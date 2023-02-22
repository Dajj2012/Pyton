n=int(input('Введите длинну'))
m=int(input('Введите ширину'))
k=int(input('Введите искомое количество'))
i=1
flag=0
while i<=n:
    if m*i==k:
        flag+=1
    i=i+1
i=1
while i<=m:
    print(n*i)
    if n*i==k:
        flag+=1
    i=i+1
if flag>0:
    print("Разлом возможен")
else:
    print("Разлом не возможен")