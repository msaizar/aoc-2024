# 0,0 0,1 0,2 0,3
# 1,0 1,1 1,2 1,3
# 2,0 2,1 2,2 2,3
# 3,0 3,1 3,2 3,3


def check_horizontal(xmas_array, i, j):
    try:
        if (
            xmas_array[i][j + 1] == "M"
            and xmas_array[i][j + 2] == "A"
            and xmas_array[i][j + 3] == "S"
        ):
            return True
    except IndexError:
        return False
    return False


def check_vertical(xmas_array, i, j):
    try:
        if (
            xmas_array[i + 1][j] == "M"
            and xmas_array[i + 2][j] == "A"
            and xmas_array[i + 3][j] == "S"
        ):
            return True
    except IndexError:
        return False
    return False


def check_diagonal_left_right(xmas_array, i, j):
    try:
        if (
            xmas_array[i + 1][j + 1] == "M"
            and xmas_array[i + 2][j + 2] == "A"
            and xmas_array[i + 3][j + 3] == "S"
        ):
            return True
    except IndexError:
        return False
    return False


def check_diagonal_right_left(xmas_array, i, j):
    try:
        if (
            xmas_array[i + 1][j - 1] == "M"
            and xmas_array[i + 2][j - 2] == "A"
            and xmas_array[i + 3][j - 3] == "S"
        ) and j > 2:
            return True
    except IndexError:
        return False
    return False


def check_backwards_horizonal(xmas_array, i, j):
    try:
        if (
            xmas_array[i][j - 1] == "M"
            and xmas_array[i][j - 2] == "A"
            and xmas_array[i][j - 3] == "S"
        ) and j > 2:
            return True
    except IndexError:
        return False
    return False


def check_backwards_vertical(xmas_array, i, j):
    try:
        if (
            xmas_array[i - 1][j] == "M"
            and xmas_array[i - 2][j] == "A"
            and xmas_array[i - 3][j] == "S"
        ) and i > 2:
            return True
    except IndexError:
        return False
    return False


def check_backwards_diagonal_left_right(xmas_array, i, j):
    try:
        if (
            (
                xmas_array[i - 1][j - 1] == "M"
                and xmas_array[i - 2][j - 2] == "A"
                and xmas_array[i - 3][j - 3] == "S"
            )
            and j > 2
            and i > 2
        ):
            return True
    except IndexError:
        return False
    return False


def check_backwards_diagonal_right_left(xmas_array, i, j):
    try:
        if (
            xmas_array[i - 1][j + 1] == "M"
            and xmas_array[i - 2][j + 2] == "A"
            and xmas_array[i - 3][j + 3] == "S"
        ) and i > 2:
            return True
    except IndexError:
        return False
    return False


with open("input.txt", "r") as file:
    data = file.readlines()
    xmas_array = []
    total = 0
    for line in data:
        xmas_array.append(list(line.rstrip()))

    for i in range(len(xmas_array)):
        for j in range(len(xmas_array[i])):
            if xmas_array[i][j] == "X":
                if check_horizontal(xmas_array, i, j):
                    total += 1
                if check_vertical(xmas_array, i, j):
                    total += 1
                if check_diagonal_left_right(xmas_array, i, j):
                    total += 1
                if check_diagonal_right_left(xmas_array, i, j):
                    total += 1
                if check_backwards_horizonal(xmas_array, i, j):
                    total += 1
                if check_backwards_vertical(xmas_array, i, j):
                    total += 1
                if check_backwards_diagonal_left_right(xmas_array, i, j):
                    total += 1
                if check_backwards_diagonal_right_left(xmas_array, i, j):
                    total += 1

    print(total)
