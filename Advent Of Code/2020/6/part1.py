import os
import time
import copy 

start = time.time()  
f = open("input.txt",'r').read().split("\n\n")

Length = 0

for i in range(len(f)):
     f[i] = f[i].replace("\n","")
     l = list(f[i])
     qs = []
     for j in range(len(f[i])):
          if l[j] in qs:
               pass
          else:
               qs.append(l[j])
     Length += len(qs)



print(f[1])

print(f)

print(Length)

end = time.time()
runtime = end - start
print(runtime)