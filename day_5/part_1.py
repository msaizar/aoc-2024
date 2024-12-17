with open("input.txt", "r") as file:
    data = file.readlines()
    rules = {}
    orders = []
    total = 0
    for line in data:
        if "|" in line:
            a, b = line.strip().split("|")
            if a not in rules:
                rules[a] = []
            rules[a].append(b)
        elif "," in line:
            correct_order = True
            order = line.strip().split(",")
            for i in range(len(order)):
                try:
                    must_be_before = rules[order[i]]
                    for previous in must_be_before:
                        try:
                            if order.index(previous) <= i:
                                correct_order = False
                        except ValueError:
                            pass
                except KeyError:
                    pass
            if correct_order:
                total += int(order[len(order) // 2])
                orders.append(order)
    print(total)
