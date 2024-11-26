print ('Блок А')
print ('1 Задание ')
def f (a):
    if a==1:
        return 1
    else:
        return a*f(a-1) #факториал
x = int(input('x: '))
n = int(input('n: '))
b = (x**n)/f(n)
print('Ответ: ', b)