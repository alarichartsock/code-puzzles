import os
import time

start = time.time()  
f = open("input.txt",'r').read().split('\n') #turns file input into a list I can work with
f.remove('')
f = f[:-1]
f = list(map(int, f)) #turns every item in list into int for easier manipulation

for i in f:
    for j in f:
        for k in f:
            if i+j+k == 2020:
                print(i*j*k)

end = time.time()
runtime = end - start
print("Time " + str(runtime)) #Benchmarks solution

