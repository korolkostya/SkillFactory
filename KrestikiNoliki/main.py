def play(count):
    """Ввод данных"""
    x = -1
    y = -1
    print("===================")
    if count%2 != 0:
        print("Ход игрока x:")
    else:
        print("Ход игрока o:")
    while x>=3 or x<0:
        try:
            x = int(input("Введите координату строки от 0 до 2:"))
        except ValueError:
            print("Необходимо ввести число от 0 до 2!")
        finally:
            continue
    while y>=3 or y<0:
        try:
            y = int(input("Введите координату столбца от 0 до 2:"))
        except ValueError:
            print("Необходимо ввести число от 0 до 2!")
        finally:
            continue
    coord = [x, y]
    return coord


def set_value(x, y, v, l):
    """Запись данных в матрицу"""
    if l[x][y] == "-":
        l[x][y] = v
        return True
    else:
        return False


def display_matrix(l):
    """Печать матрицы"""
    print("  0 1 2")
    for i in range(3):
        print(f"{i} {l[i][0]} {l[i][1]} {l[i][2]}")


def victory(l, count):
    """Проверка на выигрышь"""
    if count%2==0:
        v = "x"
    else:
        v = "o"
    for i in range(3):
        if (l[0][i] == l[1][i] == l[2][i] and l[0][i] != "-") or (l[i][0] == l[i][1] == l[i][2] and l[i][0] != "-"):
            print(f"Победа! Выиграл игрок {v}")
            return False
    if (l[0][0] == l[1][1] == l[2][2] and l[0][0] != "-") or (l[2][0] == l[1][1] == l[0][2] and l[2][0] != "-"):
        print(f"Победа! Выиграл игрок {v}")
        return False
    else:
        return True


l = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
display_matrix(l)
count = 1
v = ""

while victory(l, count):
    if count == 10:
        print("Ничья!")
        break
    coord=play(count)
    if count%2 != 0:
        v = "x"
    else:
        v = "o"
    if set_value(*coord, v, l):
        display_matrix(l)
        count += 1
    else:
        display_matrix(l)
        print("Позиция занята, повторите ход")
        continue