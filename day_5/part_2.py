def fix_order(order=[], rules={}):
    new_order = []

    for i in range(len(order)):
        print(f"Unordered element: {order[i]}")
        inserted = False
        for j in range(len(new_order)):
            if order[i] in rules and new_order[j] in rules[order[i]]:
                print(
                    f"Unordered element {order[i]} should go before {new_order[j]} according to '{order[i]}':{rules[order[i]]}"
                )
                new_order.insert(j, order[i])
                print(f"New Order: {new_order}")
                inserted = True
                break
            elif order[i] not in rules:
                print(f"Unordered element {order[i]} not in rules, appending")
                new_order.append(order[i])
                print(f"New Order: {new_order}")
                inserted = True
                break
        if not inserted:
            print(
                f"Pages in new list didn't match rules for {order[i]}, appending: '{order[i]}':{rules[order[i]]}"
            )
            new_order.append(order[i])
            print(f"New Order: {new_order}")
    print(f"Initial Order: {order} Length: {len(order)}")
    print(f"New Order: {new_order} Length: {len(new_order)}")
    return new_order


with open("input.txt", "r") as file:
    data = file.readlines()
    rules = {}
    orders = []
    total = 0
    total_incorrect = 0
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
                                break
                        except ValueError:
                            pass
                except KeyError:
                    pass
            if correct_order:
                total += int(order[len(order) // 2])
                orders.append(order)
            else:
                new_order = fix_order(order, rules)
                total_incorrect += int(new_order[len(new_order) // 2])
    print(total_incorrect)
