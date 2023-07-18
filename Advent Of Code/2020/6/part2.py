import os
import time
import copy 

start = time.time()  
f = open("input.txt",'r').read().split("\n\n")

n = 0

for i in range(len(f)):
     f[i] = f[i].split("\n")

     s = set(f[i][0])
     for j in range(len(f[i])):
          s = s & set(f[i][j])
     n += len(s)

print(str(n))

end = time.time()
runtime = end - start
print(runtime)