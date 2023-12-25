from collections import Counter
from functools import cmp_to_key

with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n')

def cardRank(c):
  rankings = {str(i):i for i in range(2,10)}
  rankings['T'] = 10
  rankings['J'] = 1
  rankings['Q'] = 11
  rankings['K'] = 12
  rankings['A'] = 13

  return rankings[c]

def compareHands(hand1, hand2):
  if hand1 == '' or hand2 == '':
    return 0 # Cards are identical and we've ran out of cards to count
  else:
    c1 = cardRank(hand1[0])
    c2 = cardRank(hand2[0])

    if c1 < c2:
      return -1
    elif c1 > c2:
      return 1
    else: # Cards are identical and we have cards to count
      return compareHands(hand1[1:], hand2[1:])

def handRank(cards):
  c = list(Counter(cards).most_common())

  hand = 0

  if c[0][1] == 5: # Five of a kind
    hand = 7
  elif c[0][1] == 4: # Four of a kind
    hand = 6
  elif (c[0][1] == 3) and (c[1][1] == 2): # Full house
    hand = 5
  elif (c[0][1] == 3) and (len(c) == 3): # Three of a kind
    hand = 4
  elif (c[0][1] == 2) and (c[1][1] == 2) and (len(c) == 3): # Two pair
    hand = 3
  elif (c[0][1] == 2) and (len(c) == 4): # One pair
    hand = 2
  elif len(c) == 5: # High card
    hand = 1

  return hand

def repl(hand, replacement):
  ret = ''

  for char in hand:
    if char == 'J':
      ret += replacement
    else:
      ret += char
  
  return ret

def rank(hand1, hand2):

  replacements = [str(i) for i in range(2,10)]
  replacements.extend(['A', 'K', 'Q', 'T', 'J'])

  hand1 = hand1[0]
  hand2 = hand2[0]

  h1 = handRank(hand1)
  h2 = handRank(hand2)

  p, p2 = '', ''

  if 'J' in hand1:
    J_count = hand1.count('J')
    for perm in replacements:
      comp = handRank(repl(hand1, perm))
      if comp > h1:
        h1 = comp
        p = repl(hand1,perm)

  if 'J' in hand2:
    J_count = hand2.count('J')
    for perm in replacements:
      comp = handRank(repl(hand2, perm))
      if comp > h2:
        h2 = comp
        p2 = repl(hand2,perm)

  if h1 < h2: # hand1 is higher in type
    return -1
  elif h1 > h2: # hand2 is higher in type
    return 1
  elif h1 == h2: # hands are the same type
    return compareHands(hand1,hand2)

puzzle = []

for line in f:
  cards, bet = line.split(" ")
  bet = int(bet)
  puzzle.append((cards,bet))

sort = sorted(puzzle, key=cmp_to_key(rank))

total = 0

for i,s in enumerate(sort):
  total += (i+1) * s[1]

print(total)