with open("input.txt", 'r', encoding="utf-8") as file:
    # turns file input into a list I can work with
    f = file.read()

    num = 14 # Switch to 4 for part 1

    for idx,char in enumerate(f):
        unique = set()
        for i in f[idx-num:idx]:
            unique.add(i)
        if len(unique) >= num:
            print(idx)
            break