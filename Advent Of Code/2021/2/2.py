f = open("input.txt", 'r').read().split('\n') # turns file input into a list I can work with

horizontal = 0
depth = 0
aim = 0

for i in f:
    # print(f"h:{horizontal}")
    # print(f"d:{depth}")
    # print(f"a:{aim}")
    print("")
    i = i.split()
    if i[0] == "forward":
        horizontal += int(i[1])
        depth = depth + (int(i[1]) * aim)
    elif i[0] == "down":
        # depth += int(i[1])
        aim += int(i[1])
    elif i[0] == "up":
        # depth -= int(i[1])
        aim -= int(i[1])

print(horizontal)
print(depth)

print(f"\n {horizontal * depth}")