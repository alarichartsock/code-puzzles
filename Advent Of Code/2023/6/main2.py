import re

with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n')

  parse = re.compile(r':\s*(\d*)\s*(\d*)\s*(\d*)\s*(\d*)')


  time = int(''.join(i for i in parse.findall(f[0])[0] if i != ''))
  dist = int(''.join(i for i in parse.findall(f[1])[0] if i != ''))

  ret = 0

  running = False

  for i in range(1,time):
    remainingtime = time - i
    travelled = remainingtime * i

    if remainingtime <= time and travelled > dist:
      ret += 1
      
    elif ret > 0:
      break

  print(ret)