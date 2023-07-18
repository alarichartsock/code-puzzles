import os
import time
import copy 

start = time.time()  
f = open("input.txt",'r').read().split()


Max = 0
seats = []

for line in f:
     line = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
     row = int(line[:7],2)
     column = int(line[7:],2)
     Max = max(p1,row*8+column)
     seats.append(row*8+column)

for i in range(max(seats)):
     if i-1 in seats and i+1 in seats and i not in seats:
          print(i)
print(p1)

end = time.time()
runtime = end - start
print(runtime)