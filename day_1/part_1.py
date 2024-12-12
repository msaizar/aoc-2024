import csv

a_list = []
b_list = []
with open("input.txt", newline="") as locations:
    location_reader = csv.reader(locations, delimiter=" ")
    for location in location_reader:
        a_list.append(location[0])
        b_list.append(location[3])

a_list.sort()
b_list.sort()

res = map(lambda x, y: abs(int(x) - int(y)), a_list, b_list)
print(sum(list(res)))
