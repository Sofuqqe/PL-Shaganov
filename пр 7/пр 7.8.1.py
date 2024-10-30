
def find_numbers(n):
    result = []
    
    for num in range(1, n + 1):
        str_num = str(num)
        divisible = True
        
        for digit in str_num:
            d = int(digit)
            if d == 0 or num % d != 0:
                divisible = False
                break
        
        if divisible:
            result.append(num)
    
    return result

# Пример использования
n = int(input('Ведите число n:'))
numbers = find_numbers(n)
print(numbers)
