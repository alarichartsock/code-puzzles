import re
from colorist import Color

def check_neighbors(arr, x, y):

  minx, maxx = 0, len(arr[0]) - 1
  miny, maxy = 0, len(arr) - 1

  neighbors = []

  for i in range(-1,2):
    for j in range(-1,2):
      if i == 0 and j == 0:
        continue
      
      newx, newy = x+i, y+j

      if (minx <= newx <= maxx) and (miny <= newy <= maxy):
        neighbors.append(arr[newy][newx])
  
  # print(arr[y][x], neighbors)

  for neighbor in neighbors:
    if neighbor in ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']:
      return True

with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n')

  # print(check_neighbors(f,1,0))

  total = 0

  s = set()

  for y,row in enumerate(f):
    num = ''
    adjacent = False
    for x,char in enumerate(row):
      s.update(char)
      if char != '.' and check_neighbors(f,x,y):
        # print(f'{char} is adjacent')
        adjacent = True
      if char.isdigit():
        num += char
      elif adjacent and num != '':
        print(f'{Color.RED}{num}{Color.OFF}{char}', end='')
        total += int(num)

        # Reset vals
        num = ''
        adjacent = False
      else:
        if num == '':
          print(char, end='')
        else:
          print(num + char,end='')
        num = ''
        adjcent = False
    
    if adjacent:
      print(f'{Color.RED}{num}{Color.OFF}')
      total += int(num)
    else:
      print(num)

  print(total)