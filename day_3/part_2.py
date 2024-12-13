import re


def check_do(data, i):
    if data[i : i + 4] == "do()":
        return True
    else:
        return False


def check_dont(data, i):
    if data[i : i + 7] == "don't()":
        return False
    else:
        return True


def check_mul(data, i):
    findings = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data[i : i + 12])
    for finding in findings:
        return int(finding[0]) * int(finding[1])


final = 0
enabled = True
with open("input.txt", "r") as file:
    data = file.read().rstrip()
    for i in range(len(data) - 1):
        if data[i] == "d":
            if not enabled:
                enabled = check_do(data, i)
            elif enabled:
                enabled = check_dont(data, i)
        elif data[i] == "m":
            if enabled:
                result = check_mul(data, i)
                if result:
                    final += result
print(final)
