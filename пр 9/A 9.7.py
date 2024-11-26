# Числа в порядке возрастания и убывания
def f(n,k):
    if n>k:
        print(k)
        return f(n,k+1)
    if n<k:
        print(k)
        return f(n,k-1)
    if n==k:
        return k
a=int(input())
b=int(input())
print(f(a,b))