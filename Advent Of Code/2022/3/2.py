with open("input.txt", 'r', encoding="utf-8") as file:
    # turns file input into a list I can work with
    f = file.read().split('\n')

    total = 0
    i = 0
    while i < len(f):
        items1 = f[i]
        items2 = f[i+1]
        items3 = f[i+2]
        
        common = list(set(items1)&set(items2)&set(items3))
        idx = ord(common)

        if idx >= 97:
            offset = idx - 96
            total += offset
        else:
            offset = idx - 65
            total += offset + 27
        i += 3
    print(total)