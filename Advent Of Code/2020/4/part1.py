import os
import time

start = time.time()  
f = open("bigboy.txt",'r').read().split("\n\n")
for i in range(len(f)):
     f[i] = f[i].split()
     for j in range(len(f[i])):
          f[i][j] = f[i][j].split(":")

validPass = 0
for i in range(len(f)):
     fields = 0
     for j in range(len(f[i])):
          if f[i][j][0] in ['ecl','pid','eyr','hcl','byr','iyr','hgt']: fields += 1
     if fields >= 7: validPass += 1

print(validPass)
end = time.time()
runtime = end - start
print(runtime)