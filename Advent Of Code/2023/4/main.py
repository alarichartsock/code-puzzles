with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n')

  ret = 0

  for line in f:
    begin,end = line.split("|")
    
    nums = [s for s in end.strip().split(" ") if s != '']

    cardnum, startrow = begin.split(":")[0][-1], begin.split(":")[1]
    winning = [s for s in startrow.strip().split(" ") if s != '']

    pts = .5

    for num in nums:
      if num in winning:
        pts = pts * 2

    if pts >= 1:
      ret += pts

  print(ret)