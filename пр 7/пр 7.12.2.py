#2
import math

def mediana(a, b, c):
  #Вычисляет медиану треугольника к стороне a.
  return math.sqrt((2 * b**2 + 2 * c**2 - a**2) / 4)

def main():
  a = float(input("Введите длину стороны a: "))
  b = float(input("Введите длину стороны b: "))
  c = float(input("Введите длину стороны c: "))

  # Вычисление медиан исходного треугольника
  ma = mediana(a, b, c)
  mb = mediana(b, a, c)
  mc = mediana(c, a, b)

  # Вычисление сторон нового треугольника (медиан)
  new_a = mediana(ma, mb, mc)
  new_b = mediana(mb, ma, mc)
  new_c = mediana(mc, ma, mb)

  print("Длины сторон нового треугольника (медиан):")
  print(f"a': {new_a}")
  print(f"b': {new_b}")
  print(f"c': {new_c}")

main()