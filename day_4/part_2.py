# 0,0 0,1 0,2 0,3
# 1,0 1,1 1,2 1,3
# 2,0 2,1 2,2 2,3
# 3,0 3,1 3,2 3,3


def check_xmas(xmas_array, i, j):
    try:
        if (
            xmas_array[i - 1][j - 1] in ["M", "S"]
            and xmas_array[i + 1][j + 1] in ["M", "S"]
            and xmas_array[i - 1][j - 1] != xmas_array[i + 1][j + 1]
            and xmas_array[i + 1][j - 1] in ["M", "S"]
            and xmas_array[i - 1][j + 1] in ["M", "S"]
            and xmas_array[i + 1][j - 1] != xmas_array[i - 1][j + 1]
            and i > 0
            and j > 0
        ):
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
            if xmas_array[i][j] == "A":
                if check_xmas(xmas_array, i, j):
                    total += 1

    print(total)
