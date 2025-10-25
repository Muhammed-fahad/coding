arr = [[1,0,0,1],
       [0,1,0,1],
       [1,0,1,0],
       [0,1,0,1]]

def islandCheck(i,j):
  # Chech up
  if(arr[i-1][j] == 1):
    return False
  # check Down
  elif(arr[i+1][j] == 1):
    return False
  
  # check left
  elif(arr[i][j-1] == 1):
    return False
  
  # check right
  elif(arr[i][j+1] == 1):
    return False
  
  return True

countIsland = 0
for i in range(len(arr)):
  for j in range(len(arr)):
    if(i!=0 and j!=0 and j!=len(arr)-1 and i!=len(arr)-1):
      if(islandCheck(i,j)):
        countIsland+=1

print(countIsland)