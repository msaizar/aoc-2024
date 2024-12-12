import csv

safe = 0


def check_report(report):
    if (report == sorted(report) or report == sorted(report, reverse=True)) and all(
        abs(int(report[i]) - int(report[i + 1])) in [1, 2, 3]
        for i in range(len(report) - 1)
    ):
        return True
    return False


with open("input.txt", newline="") as reports:
    report_reader = csv.reader(reports, delimiter=" ")

    for report in report_reader:
        report = list(map(lambda x: int(x), report))
        if check_report(report):
            safe += 1

print(safe)
