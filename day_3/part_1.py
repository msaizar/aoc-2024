import re

final = 0
with open("input.txt", "r") as file:
    data = file.read().rstrip()
    findings = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    for finding in findings:
        final += int(finding[0]) * int(finding[1])
print(final)
