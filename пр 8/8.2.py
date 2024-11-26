from random import randint
print('1Задание')
n=int(input())
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        b.append(randint(1,100))
    a.append(b)
print(a)
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
s=0
for i in range(n):
    for j in range(i+1,n):
        s+=a[i][j]
print(s)
print('2 Задание')
n=int(input())#Столбцы
m=int(input())#Строки
a=[]
for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(1,100))
    a.append(b)
for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')
    print()
for i in a:
    mn=0
    mx=0
    for j in range(len(i)):
        if i[j]<i[mn]:
            mn=j
        if i[j]>i[mx]:
            mx=j
    i[0],i[mx]=i[mx],i[0]
    i[mn],i[-1]=i[-1],i[mn]
print(a)