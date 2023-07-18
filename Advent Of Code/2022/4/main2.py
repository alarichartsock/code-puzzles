def range_overlap(range1, range2):
    """Whether range1 and range2 overlap."""
    x1, x2 = range1.start, range1.stop
    y1, y2 = range2.start, range2.stop
    return x1 <= y2 and y1 <= x2

with open("input.txt", 'r', encoding="utf-8") as file:
    # turns file input into a list I can work with
    f = file.read().split('\n')

    for i,rng in enumerate(f):
        f[i] = rng.split(",")
        for j,r in enumerate(f[i]):
            f[i][j] = r.split("-")

    total = 0

    for i,r in enumerate(f):
        r1 = range(int(r[0][0]),int(r[0][1]))
        r2 = range(int(r[1][0]),int(r[1][1]))

        if range_overlap(r1, r2):
            total += 1
        elif range_overlap(r2,r1):
            total += 1

    print(total)