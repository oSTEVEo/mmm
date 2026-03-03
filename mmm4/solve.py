from random import randrange
import matrix_math

MACHINERY_NOYL = 1e-9

def linear():
    print("Решаем ax = b, введите коэффициенты:")
    try:
        a = float(input("a = "))
        b = float(input("b = "))
    except ValueError:
        print("Неверно введено число.")
        return
    
    if a == 0:
        if b == 0:
            print("Уравнение имеет бесконечно много решений.")
        else:
            print("Уравнение не имеет решений.")
    else:
        x = b / a
        print(f"x = {x}")

def square():
    print("Решаем ax^2 + bx + c = 0, введите коэффициенты:")
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
    except ValueError:
        print("Неверно введено число.")
        return

    if a == 0:
        if b == 0:
            if c == 0:
                print("Уравнение имеет бесконечно много решений")
            else:
                print("Уравнение не имеет решений")
        else:
            x = -c / b
            print(f"Линейное уравнение, x = {x}")
    else:
        D = b**2 - 4*a*c
        if D < 0:
            print("Действительных корней нет (D < 0).")
        elif D == 0:
            x = -b / (2*a)
            print(f"Один корень (D = 0): x = {x}")
        else:
            x1 = (-b + D**0.5) / (2*a)
            x2 = (-b - D**0.5) / (2*a)
            print(f"Два корня: x1 = {x1}, x2 = {x2}")

def linear_system():
    print("Решаем СЛАУ")
    try:
        m = int(input("Количество строк и неизвестных: "))
        if m<=0:
            print(">0")
            return
        random_choice = input("Ввести случайные коэффициенты? [Y/n]")
        if random_choice in ("Д", "д", "Y", "y", ""):
            min_val = 0
            max_val = 100
            matrix = [[randrange(min_val, max_val) for _ in range(m+1)] for _ in range(m)]
            for row in matrix:
                print(f"{row[:-1]} = {row[-1]}")    
        else:
            print("Не реализованно.")
            return
    except ValueError:
        print("Неверно введено число.")
        return
    
    delta = matrix_math.determinant([row[:-1] for row in matrix])
    if delta == MACHINERY_NOYL:
        print("Определитель системы равен нулю, система система вырождена.")
        return
    
    solutions = []
    for column_to_exclude in range(m):
        deltaMatrix = [row[:column_to_exclude] + [row[-1]] + row[column_to_exclude+1:-1] for row in matrix]
        solutions.append(matrix_math.determinant(deltaMatrix)/delta)
    
    for i in range(m):
        print(f"x{i+1} = {solutions[i]}")


def matrix_raising():
    def print_matrix(matrix):
        for row in matrix:
            print(row)
        return

    print("Возведение матрицы в степень")
    try:
        n = int(input("Размерность квадратной матрицы (n): "))
        if n <= 0:
            print("Размерность должна быть положительной.")
            return
    except ValueError:
        print("Ошибка: введите целое число.")
        return
    
    random_choice = input("Ввести случайные коэффициенты? [Y/n]: ").strip().lower()
    if random_choice in ("Д", "д", "Y", "y", ""):
        min_val = 0
        max_val = 10
        matrix = [[randrange(min_val, max_val) for _ in range(n)] for _ in range(n)]
        print_matrix(matrix)
    else:
        ...
    
    try:
        power = int(input("Степень (целое неотрицательное число): "))
        if power < 0:
            print("Степень должна быть неотрицательной.")
            return
    except ValueError:
        print("Ошибка: введите целое число.")
        return
    
    result = matrix_math.pow(matrix, power)
    print(f"\nМатрица в степени {power}:")
    print_matrix(result)