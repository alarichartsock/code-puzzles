import os
import time

start = time.time()  
f = open("input.txt",'r').read().split('\n') # turns file input into a list I can work with
for i in range(len(f)):
     f[i] = list(f[i])
width = len(f[1])
height = len(f)

def traverse(dx,dy):
     finished = False
     trees = 0
     x = 0
     y = 0
     while(finished == False):
          if ( (x + dx) >= width): 
               x += dx
               y += dy
          else:
               x += dx
               y += dy
          if(f[y][x%width] == '#'): trees += 1
          if (y+1  >= height): finished = True
     return trees

one = traverse(1,1)
two = traverse(3,1)
three = traverse(5,1)
four = traverse(7,1)
five = traverse(1,2)

print(two) # part 1
print(one*two*three*four*five) # part 2

end = time.time()
runtime = end - start
print(runtime)