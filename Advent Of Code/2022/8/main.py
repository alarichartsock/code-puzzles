with open('input.txt') as file:
    lines = file.read().splitlines()

    forest = [list(map(int, str(line))) for line in lines]

    vis = 0

    for y, line in enumerate(forest):
        for x, tree in enumerate(line):
            left = line[:x]
            right = line[x+1:]
            top = [row[x] for row in forest[:y]]
            bottom = [row[x] for row in forest[y+1:]]

            if (max(left, default=-1) < tree) or (max(right, default=-1) < tree) or (max(top, default=-1) < tree) or (max(bottom, default=-1) < tree):
                vis += 1