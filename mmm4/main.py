"""
Решить:
1. ax=b
2. ax^2+bx+c = 0
3. Линейная система
4. A^N, где A - матрица
"""

from menu import Menu
import solve
menu = Menu()

menu.add("Линейное уравнение", solve.linear)
menu.add("Квадратное уравнение", solve.square)
menu.add("Линейная система", solve.linear_system)
menu.add("Возведение матрицы в степень", solve.matrix_raising)


def main():
    try:
        variant = int(input(f"Введите, что вы хотите решить:\n{menu.get_readable_menu()} >>> "))
    except ValueError:
        print("Введите число")
        return
    menu.run(variant)

if __name__ == "__main__":
    main()