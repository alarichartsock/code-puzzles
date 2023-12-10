import re
from colorist import Color

def get_neighbors(arr, x, y):
  minx, maxx = 0, len(arr[0]) - 1
  miny, maxy = 0, len(arr) - 1

  neighbors = []

  for i in range(-1,2):
    for j in range(-1,2):
      if i == 0 and j == 0:
        continue
      
      newx, newy = x+i, y+j

      if (minx <= newx <= maxx) and (miny <= newy <= maxy):
        if arr[newy][newx].isdigit():
          neighbors.append(((newx,newy),arr[newy][newx]))

  return neighbors
  
def find_closest_tuple(tuples, target):
    # Find the tuple with the closest second element to the target
    return min(tuples, key=lambda x: abs(x[1] - target))

with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n')

  total = 0

  s = set()

  for y,row in enumerate(f):
    
    for x,char in enumerate(row):
      if char == '*':
        found_nums = set()
        for coords,neighbor in get_neighbors(f,x,y):
          foundx = coords[0]
          foundy = coords[1]
          numbers_with_positions = [(match.group(), match.start()) for match in re.finditer(r'\d+', f[foundy])]
          
          found_nums.add(int(find_closest_tuple(numbers_with_positions, foundx)[0]))
        
        list_nums = list(found_nums)

        if len(list_nums) == 2:
          total += list_nums[0] * list_nums[1]
        
  print(total)