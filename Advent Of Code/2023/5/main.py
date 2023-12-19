with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n\n')

  vals = []

  for line in f:
    vals.append(line.split("\n"))

  seeds = vals[0][0].split(":")[1].strip().split(" ")
  maps = [[val.strip().split(" ") for val in vals[i][1:]] for i in range(1,8)] 

  starts = [int(i) for i in seeds]

  print(starts)

  for m in maps:
    new = []

    for r in m:
      r = [int(i) for i in r]
      d,s,r = r[0], r[1], r[2]

      src = range(s,s+r)
      dest = range(d,d+r)

      for i in range(len(starts) - 1, -1, -1):
        start = starts[i]
        if start in src:
          end = abs(start - s) + d
          new.append(end)
          del starts[i]

    for start in starts:
      new.append(start)
    
    starts = new

  print(min(starts))