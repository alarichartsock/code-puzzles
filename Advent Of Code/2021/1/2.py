f = open("input.txt", 'r').read().split('\n') # turns file input into a list I can work with

for i in range(len(f)):
    f[i] = int(f[i])

increased = 0 

for i in range(len(f)):

    window1 = 0
    window2 = 0

    for j in range(3):
        try:
            window1 += f[i+j]
            window2 += f[i+j+1]
        except:
            pass
    if window1 < window2:
        increased += 1
    
print(increased)