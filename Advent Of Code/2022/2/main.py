def transform_rock(i):
    """Maps rps code to actual value"""
    if i in ('A', 'X'):
        return 'r','lose'
    if i in ('B', 'Y'):
        return 'p','draw'
    if i in ('C', 'Z'):
        return 's','win'


with open("input.txt", 'r', encoding="utf-8") as file:
    # turns file input into a list I can work with
    f = file.read().split('\n')[:-1]

    print(f)

    TOTAL = 0

    for game in f:
        game = game.split(" ")
        LEFT_VAL,GARB = transform_rock((game[0]))
        RIGHT_VAL,OUTCOME = transform_rock((game[1]))

        # BEGIN PART 2
        if OUTCOME == 'draw':
            RIGHT_VAL = LEFT_VAL
        elif OUTCOME == 'win':
            if LEFT_VAL == 'r':
                RIGHT_VAL = 'p'
            elif LEFT_VAL == 'p':
                RIGHT_VAL ='s'
            elif LEFT_VAL == 's':
                RIGHT_VAL = 'r'
        elif OUTCOME == 'lose':
            if LEFT_VAL == 'r':
                RIGHT_VAL = 's'
            elif LEFT_VAL == 'p':
                RIGHT_VAL ='r'
            elif LEFT_VAL == 's':
                RIGHT_VAL = 'p'
        # END PART 2

        if LEFT_VAL == RIGHT_VAL:
            TOTAL += 3
        elif LEFT_VAL == 'r':
            if RIGHT_VAL == 'p':
                TOTAL += 6
        elif LEFT_VAL == 'p':
            if RIGHT_VAL == 's':
                TOTAL += 6
        elif LEFT_VAL == 's':
            if RIGHT_VAL == 'r':
                TOTAL += 6

        if RIGHT_VAL == 'r':
            TOTAL += 1
        elif RIGHT_VAL == 'p':
            TOTAL += 2
        elif RIGHT_VAL == 's':
            TOTAL += 3
    print(TOTAL)