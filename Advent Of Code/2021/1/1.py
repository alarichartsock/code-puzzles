f = open("input.txt", 'r').read().split('\n') # turns file input into a list I can work with

for i in range(len(f)):
    f[i] = int(f[i])

increased = 0 

for i in range(len(f)-1):
    if f[i+1] > f[i]:
        increased += 1