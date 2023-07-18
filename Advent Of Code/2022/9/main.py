def showRope(xrope,yrope,tailx,taily):

    maxx = max(xrope,tailx)
    maxy = max(yrope,taily)
    arr = [["." for pix in range(maxx+2)] for line in range(maxy+2)]

    arr[yrope][xrope] = "H"
    arr[taily][tailx] = "T"
    arr[0][0] = "s"

    arr.reverse()

    print("--")
    for line in arr:
        p = "".join(line)
        if p is not None: print(p)

with open('input.txt') as file:
    lines = [line.split(" ") for line in file.read().splitlines()]
    
    headx = 0
    heady = 0

    tailx = 0
    taily = 0

    for line in lines:
        showRope(headx, heady, tailx, taily)

        # Move head of the rope first
        if line[0] == "D":
            heady -= int(line[1])
        elif line[0] == "U":
            heady += int(line[1])
        elif line[0] == "L":
            headx -= int(line[1])
        elif line[0] == "R":
            headx += int(line[1])
        
        if taily not in range(heady-1,heady+2):
            diff = heady - taily
            if diff > 0: diff -= 1
            else: diff += 1
            taily += diff

        if tailx not in range(headx-1,headx+2):
            diff = headx - tailx
            if diff > 0: diff -= 1
            else: diff += 1
            tailx += diff

