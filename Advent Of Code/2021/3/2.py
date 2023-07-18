f = open("test.txt", 'r').read().split('\n') # turns file input into a list I can work with

o2 = ''
co2scrubber = ''

for i in range(len(f[0])):
    one = 0
    zero = 0
    for j in range(len(f)):

        
        if f[j][i] == "1":
            one += 1
        else:
            zero += 1
    

print(int(o2,2))
print(int(co2scrubber,2))