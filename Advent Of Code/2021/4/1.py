f = open("input.txt", 'r').read().split('\n') # turns file input into a list I can work with

drawn = f[0].split(",")
for i in range(len(drawn)):
    drawn[i] = int(drawn[i])

# print(f[2:])

del f[0]

boards = []
board = []
for i in range(len(f[2:])):
    if f[i] == "":
        boards.append(board)
        board = []
    else:
        board.append(f[i].split())

del boards[0]

for i in boards:
    for j in i:
        for k in range(len(j)):
            j[k] = int(j[k])

def verifyDone(nums,bingoBoard):
    def verifyRow(nums,bingoRow):
        for i in bingoRow:
            if i in nums:
                pass
            else:
                return False

    for i in bingoBoard:
        if set(i).issubset(nums): return True
    diagonal1 = [r[~i] for i, r in enumerate(bingoBoard)]
    if set(diagonal1).issubset(nums): return True
    diagonal2 = [r[i] for i, r in enumerate(bingoBoard)]
    if set(diagonal2).issubset(nums): return True

    for i in range(len(bingoBoard)):
        row = []
        for j in range(len(bingoBoard[i])):
            row.append(bingoBoard[j][i])
        if set(row).issubset(nums): return True

def calculateScore(nums,board):
    score = 0
    for i in board:
        for j in range(len(i)):
            if i[j] in nums:
                pass
            else:
                score += i[j]
    
    return score

def findBoard():
    for i in range(1,len(drawn)):
        for j in boards:
            if verifyDone(drawn[:i],j):
                print("!!DONE!!")
                print(j)
                print(f'SCORE: {calculateScore(drawn[:i],j) * drawn[:i].pop(-1)}')
                print("!!DONE!!")
                boards.remove(j)

findBoard()