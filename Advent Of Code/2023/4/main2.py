with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n')

  cardvals = []

  def count(line):
    begin,end = line.split("|")
    nums = [s for s in end.strip().split(" ") if s != '']
    cardnum, startrow = begin.split(":")[0][-1], begin.split(":")[1]
    winning = [s for s in startrow.strip().split(" ") if s != '']
    pts = 0
    for num in nums:
      if num in winning:
        pts += 1
    return pts

  for line in f:
    cardvals.append(count(line))
  
  cards = [1 for i in range(len(f))] 

  ret = len(cardvals)

  i = 0

  while i < len(cardvals):
    value = cardvals[i]
    card = cards[i]

    for j in range(card):
      for k in range(int(value)):
        if i+k+1 < len(cards):
          cards[i+k+1] += 1
          ret += 1

    i += 1
  print(ret)