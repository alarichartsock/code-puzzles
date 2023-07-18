import os
import time
import re

start = time.time()  
f = open("input.txt",'r').read().split("\n\n")
for i in range(len(f)):
     f[i] = f[i].split()
     for j in range(len(f[i])):
          f[i][j] = f[i][j].split(":")

def validate(lbl,val):
     if lbl == 'pid':
          return re.match(r"^\d{9}$",val)
     elif lbl == 'eyr':
          return (2020 <= int(val) <= 2030)
     elif lbl == 'hcl':
          return re.match(r"^#[0-9a-f]{6}$",val)
     elif lbl == 'byr':
          return (1920 <= int(val) <= 2002)
     elif lbl == 'iyr':
          return (2010 <= int(val) <= 2020)
     elif lbl == 'hgt':
          return (val[-2:]=="cm" and 150<=int(val[:-2])<=193 or val[-2:]=="in" and 59<=int(val[:-2])<=76)
     elif lbl == 'ecl':
          return val in ['amb','blu','brn','gry','grn','hzl','oth']

validPass = 0
for i in range(len(f)):
     fields = 0
     for j in range(len(f[i])):
          if validate(f[i][j][0],f[i][j][1]): fields += 1
     if fields >= 7: validPass += 1

print(validPass)
end = time.time()
runtime = end - start
print(runtime)