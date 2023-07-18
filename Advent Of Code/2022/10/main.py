def printScreen(crt):
    count = 0
    for idx,pix in enumerate(crt):
        print(pix,end="")
        count +=1
        if count == 40:
            print("")
            count = 0

with open('test.txt') as file:
    lines = file.read().splitlines()
    lines = [line.split(" ") for line in lines]

    vals = []
    val = 1

    for line in lines:
        if line[0] == 'noop':
            vals.append(val)
        elif line[0] == 'addx':
            vals.append(val)
            vals.append(val)
            val += int(line[1])
    
    # Part 1
    indices = [20,60,100,140,180,220]
    sol = 0
    for indice in indices:
        sol += vals[indice] * indice
    print(sol)

    # Part 2
    crt = ["" for i in range(241)]

    for idx,val in enumerate(vals):
        rng = idx % 40
        if val in [rng-1, rng, rng+1]:
            crt[idx] = "#"
        else:
            crt[idx] = '.'
    
    printScreen((crt))
