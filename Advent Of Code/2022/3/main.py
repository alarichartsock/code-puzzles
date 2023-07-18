with open("input.txt", 'r', encoding="utf-8") as file:
    # turns file input into a list I can work with
    f = file.read().split('\n')

    total = 0

    for items in f:
        mid = len(items)//2

        item1 = items[:mid]
        item2 = items[mid:]
        common = list(set(item1)&set(item2))

        for priority in common:
            idx = ord(priority)

            if idx >= 97:
                offset = idx - 96
                total += offset
            else:
                offset = idx - 65
                total += offset + 27

    print(total)
