#4.2
a = [int(l) for l in input().split()]
b = []
for i in a:
    if i % 2 == 1:
        b.append(i)
if len(b) > 0:
    print(sorted(b, reverse = True))
else:
    print('Нет')