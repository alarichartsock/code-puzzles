from collections import Counter
from functools import cmp_to_key

with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n')

def cardRank(c):
  rankings = {str(i):i-1 for i in range(2,10)}
  rankings['T'] = 10
  rankings['J'] = 11
  rankings['Q'] = 12
  rankings['K'] = 13
  rankings['A'] = 14

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

def rank(hand1, hand2):
  h1 = handRank(hand1[0])
  h2 = handRank(hand2[0])

  if h1 < h2: # hand1 is higher in type
    return -1
  elif h1 > h2: # hand2 is higher in type
    return 1
  elif h1 == h2: # hands are the same type
    return compareHands(hand1[0],hand2[0])

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