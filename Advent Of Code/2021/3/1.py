f = open("input.txt", 'r').read().split('\n') # turns file input into a list I can work with

gamma = ''
epsilon = ''

for i in range(len(f[0])):
    one = 0
    zero = 0
    for j in range(len(f)):
        if f[j][i] == "1":
            one += 1
        else:
            zero += 1
    if one > zero:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(gamma)
print(epsilon)

print(int(gamma,2))
print(int(epsilon,2))

