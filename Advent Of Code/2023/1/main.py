with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n')

  ret = 0

  for line in f:
    first = None
    last = None

    for char in line:
      if char in ['0','1','2','3','4','5','6','7','8','9']:
        if first:
          last = char
        else:
          first = char
          last = char

    print(line)
    print(first, last)

    ret += int(first + last)
  
  print(ret)
    
  
