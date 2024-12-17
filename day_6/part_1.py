def draw_xmas_map(xmas_map):
    for i in range(len(xmas_map)):
        for j in range(len(xmas_map[i])):
            print(xmas_map[i][j], end="")
        print("")
    print("")


def move_guard(x, y, guard_type, xmas_map):
    exited = False
    total_visited = 0
    while not exited:
        if guard_type == "^":
            if x == 0:
                exited = True
                if xmas_map[x][y] != "X":
                    xmas_map[x][y] = "X"
                    total_visited += 1
            else:
                if xmas_map[x - 1][y] == "#":
                    guard_type = ">"
                else:
                    if xmas_map[x][y] != "X":
                        xmas_map[x][y] = "X"
                        total_visited += 1
                    x = x - 1
        elif guard_type == "v":
            if x == len(xmas_map) - 1:
                exited = True
                if xmas_map[x][y] != "X":
                    xmas_map[x][y] = "X"
                    total_visited += 1
            else:
                if xmas_map[x + 1][y] == "#":
                    guard_type = "<"
                else:
                    if xmas_map[x][y] != "X":
                        xmas_map[x][y] = "X"
                        total_visited += 1
                    x = x + 1
        elif guard_type == "<":
            if y == 0:
                exited = True
                if xmas_map[x][y] != "X":
                    xmas_map[x][y] = "X"
                    total_visited += 1
            else:
                if xmas_map[x][y - 1] == "#":
                    guard_type = "^"
                else:
                    if xmas_map[x][y] != "X":
                        total_visited += 1
                        xmas_map[x][y] = "X"
                    y = y - 1
        elif guard_type == ">":
            if y == len(xmas_map[x]) - 1:
                exited = True
                if xmas_map[x][y] != "X":
                    xmas_map[x][y] = "X"
                    total_visited += 1
            else:
                if xmas_map[x][y + 1] == "#":
                    guard_type = "v"
                else:
                    if xmas_map[x][y] != "X":
                        xmas_map[x][y] = "X"
                        total_visited += 1
                    y = y + 1
    return total_visited


def find_guard(xmas_map):
    for i in range(len(xmas_map)):
        for j in range(len(xmas_map[i])):
            if xmas_map[i][j] in ["^", "v", "<", ">"]:
                return (i, j, xmas_map[i][j])


with open("input.txt", "r") as file:
    data = file.readlines()
    xmas_map = []
    for line in data:
        xmas_map.append(list(line.strip()))

    draw_xmas_map(xmas_map)
    x, y, guard_type = find_guard(xmas_map)
    total_visited = move_guard(x, y, guard_type, xmas_map)
    print(total_visited)
