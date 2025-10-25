arr = [3, 4, 2, 6, 9, 4]
n = len(arr)
for i in range(n-1):
  val = arr[i+1]
  for j in range (i+1 , n):
    if (arr[j] >= val):
      val=arr[j]
    else:
      if(arr[i]<val):
        arr[i] = val
        break
      else:
        arr[i] = -1
        
if(arr[-2]>arr[-1]):
    arr[-2] = -1
else:
    arr[-2] = arr[-1]
    
arr[-1] = -1
print(arr)