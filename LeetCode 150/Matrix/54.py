
def move(matrix,prev,cur,visited):
  m = len(matrix[0])
  n = len(matrix)

  i1, j1 = prev
  i2, j2 = cur

  for a in range(len(matrix)):
    for b in range(len(matrix[0])):
      print(f'{a} {b}')

  if abs(i2 - i1) > 0:

    print("Traveling vertically")

  if abs(j2 - j1) > 0:
    
    print("Traveling horizontally")




l = [[1,2,3],[4,5,6],[7,8,9]]

move(l,[0,0],[0,1])