import re

with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n')

  parse = re.compile(r':\s*(\d*)\s*(\d*)\s*(\d*)\s*(\d*)')

  time = [int(i) for i in parse.findall(f[0])[0] if i != '']
  dist = [int(i) for i in parse.findall(f[1])[0] if i != '']

  rets = []

  for t, d in zip(time, dist):
    ret = 0
    for i in range(1,t):
      remainingtime = t - i
      travelled = remainingtime * i

      if remainingtime <= t and travelled > d:
        ret += 1
    rets.append(ret)

  tot = 1

  for i in rets:
    tot *= i
  
  print(tot)