with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n\n')

vals = []
for line in f:
  vals.append(line.split("\n"))

seeds = vals[0][0].split(":")[1].strip().split(" ")

maps = [[val.strip().split(" ") for val in vals[i][1:]] for i in range(1,8)] 

seedints = [(int(seeds[i]), int(seeds[i]) + int(seeds[i+1])) for i in range(0,len(seeds),2)]

mapints = [[[int(i) for i in j] for j in k] for k in maps]

for m in mapints:
  new = []

  while seedints:
    start, end = seedints.pop()
    for a, b, R in m:
      os = max(start, b)
      oe = min(end, b + R)
      if os < oe:
        new.append((os - b + a, oe - b + a))
        if os > start:
          seedints.append((start, os))
        if end > oe:
          seedints.append((oe,end))
        break
    else:
      new.append((start,end))
  seedints = new

print(min(seedints)[0])