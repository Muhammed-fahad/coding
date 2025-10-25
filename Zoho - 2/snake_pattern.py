arr = [[1,2,3],[4,5,6],[7,8,9]]
#  1 2 3 6 5 4 7 8 9

for i in range(len(arr)):
  if (i+1) % 2 == 1:
    for j in range(len(arr[0])):
      print(arr[i][j],end=" ")
  
  else:
    for j in range(len(arr[0])-1,-1,-1):
      print(arr[i][j],end=" ")