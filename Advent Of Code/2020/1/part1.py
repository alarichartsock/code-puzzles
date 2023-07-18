import time

start = time.time()  
f = open("input.txt", 'r').read().split('\n') # turns file input into a list I can work with
f.remove('')
f = f[:-1]

for i in range(len(f)):
    inputval = int(f[i])
    targetval = 2020 - inputval
    if str(targetval) in f:
        result = inputval * targetval
        print("RESULT: " + str(result))   
end = time.time()
runtime = end - start
print(runtime)
