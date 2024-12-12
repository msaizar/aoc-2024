import csv

a_list = []
b_list = []
with open("input.txt", newline="") as locations:
    location_reader = csv.reader(locations, delimiter=" ")
    for location in location_reader:
        a_list.append(int(location[0]))
        b_list.append(int(location[3]))

a_list.sort()
b_list.sort()
similarity = 0

for element in a_list:
    similarity += element * b_list.count(element)

print(similarity)
