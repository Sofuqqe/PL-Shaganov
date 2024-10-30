#1
def divisors_sum(n):
 #Вычисляет сумму всех делителей числа, кроме самого числа.
 sum_divisors = 1
 for i in range(2, int(n**0.5) + 1):
  if n % i == 0:
   sum_divisors += i
   if i != n // i:
    sum_divisors += n // i
 return sum_divisors

def find_friendly_pairs(N):
 #Находит все пары дружественных чисел, не превышающие N.
 friendly_pairs = []
 for a in range(2, N + 1):
  for b in range(a + 1, N + 1):
   if divisors_sum(a) == b and divisors_sum(b) == a:
    friendly_pairs.append((a, b))
 return friendly_pairs

N = int(input("Введите число N: "))

# Находим пары дружественных чисел
pairs = find_friendly_pairs(N)

if pairs:
 print("Пары дружественных чисел, не превышающие", N, ":", pairs)
else:
 print("Нет пар дружественных чисел, не превышающих", N)
