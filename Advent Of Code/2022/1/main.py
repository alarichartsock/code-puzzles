with open("input.txt", 'r',encoding="utf-8") as file:
    f = file.read().split('\n')  # turns file input into a list I can work with

    arr = []
    subarr = []

    for index, item in enumerate(f):
        if item == "":
            arr.append(subarr)
            subarr = []
        else:
            subarr.append(int(item))

    sums = []

    for index, row in enumerate(arr):
        total = 0
        for calorie in row:
            total += calorie
        sums.append(total)

    sums = sorted(sums)

    answer1 = sums[-1]
    answer2 = sums[-1] + sums[-2] + sums[-3]

    print(answer1)
    print(answer2)
