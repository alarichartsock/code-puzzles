import regex as re

parsed = []

with open("crates.txt", 'r', encoding="utf-8") as file:
    # turns file input into a list I can work with
    f = file.read().split('\n')[:-1]
    
    fj = []

    for fi in f:
        sinceCrate = 0
        parsedRow = []
        for char in fi:
            if char == " ":
                sinceCrate += 1
            elif char in ['[', ']']:
                sinceCrate = 0
            else:
                sinceCrate = 0
                parsedRow.append(char)
            if sinceCrate == 4:
                parsedRow.append("")
                sinceCrate = 0
        parsed.append(parsedRow)

nums = []

with open("directions.txt", 'r', encoding="utf-8") as file:
    # turns file input into a list I can work with
    f = file.read().split('\n')

    pat = r'move ([0-9]+) from ([0-9]+) to ([0-9]+)'
    nums = [re.match(pat,fi)[1:] for fi in f]

stacks = [[] for i in range(9)]

for i in parsed:
    for idx,crate in enumerate(i):
        stacks[idx].insert(0,crate)

stacks = [list(filter(None, stack)) for stack in stacks]


for num in nums:
    amount = int(num[0])
    fro = int(num[1])-1
    to = int(num[2])-1

    for i in range(amount):
        popped = stacks[fro].pop()
        stacks[to].append(popped)

# Sol 1
print(stacks)

