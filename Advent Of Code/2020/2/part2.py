import os
import time
import re

start = time.time()  
f = open("input.txt",'r').read().split('\n') # turns file input into a list I can work with
f.remove('')
for i in range(len(f)):
     f[i] = f[i].split(": ")
for i in range(len(f)):
     chars = f[i][1]
     f[i][0] = f[i][0].split("-")
     f[i][0][1] = f[i][0][1].split(" ")
     
validpass = 0
for i in range(len(f)):
     lowerbound = int(f[i][0][0])
     upperbound = int(f[i][0][1][0])
     char = f[i][0][1][1]
     passw = list(f[i][1])
     print(passw)
     if (passw[lowerbound - 1] == char) ^ ( passw[upperbound - 1] == char):
          validpass = validpass + 1
     
print(validpass)
end = time.time()
runtime = end - start
print(runtime)
