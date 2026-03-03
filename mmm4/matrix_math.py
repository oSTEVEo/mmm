def determinant(matrix) -> float:
    if not matrix:
        raise ValueError("Матрица не должна быть пустой")

    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("Матрица должна быть квадратной")

    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        sign = 1 if j % 2 == 0 else -1
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += sign * matrix[0][j] * determinant(minor)

    return det


def multiply(A, B):
    """Умножение двух матриц (обе должны быть квадратными одного размера)."""
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # Скалярное произведение i-й строки A и j-го столбца B
            s = 0
            for k in range(n):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C


def pow(matrix, power):
    """Возвращает matrix ** power для целого power >= 0."""
    n = len(matrix)
    if power == 0:
        # np.eye()
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    result = None
    base = matrix
    p = power

    while p > 0:
        if p % 2 == 1:
            if result is None:
                result = base
            else:
                result = multiply(result, base)
        base = multiply(base, base)
        p = p // 2
    return result