
def divide_row_by_diagonal(matrix, k):
    """Разделяет элементы k-й строки матрицы на диагональный элемент этой строки."""
    n = matrix.shape[0]  # Порядок матрицы
    if k < 0 or k >= n:
        raise ValueError("Индекс строки k должен быть в пределах от 0 до n-1.")
    
    diagonal_element = matrix[k, k]  # Находим диагональный элемент
    if diagonal_element == 0:
        raise ValueError("Диагональный элемент равен нулю, деление невозможно.")
    
    # Разделяем элементы k-й строки на диагональный элемент
    matrix[k] = matrix[k] / diagonal_element
    return matrix

# Пример использования
n = 3  # Порядок матрицы
k = 1  # Номер строки, которую нужно обработать (0-индексация)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Исходная матрица:")
print(matrix)

result_matrix = divide_row_by_diagonal(matrix, k)

print("Матрица после обработки:")
print(result_matrix)
