import re

with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n')

  findgame = re.compile(r'(\d+:)')
  fr,fg,fb = re.compile(r'(\d+) (?=red)'), re.compile(r'(\d+) (?=green)'), re.compile(r'(\d+) (?=blue)')

  part1 = 0
  part2 = 0

  for line in f:
    gameid = findgame.findall(line)[0][:-1]
    mred, mgreen, mblue = max([int(r) for r in fr.findall(line)]), max([int(g) for g in fg.findall(line)]), max([int(b) for b in fb.findall(line)])

    if (maxred > 12) or (maxgreen > 13) or (maxblue > 14):
      pass
    else:
      part1 += int(gameid)

    power = mred * mgreen * mblue

    part2 += power

  print(part1)
  print(part2)

