arr = [0,1,2,2,3,0,4,2]
value = 2
v = 0
for i in range(len(arr)):
  if arr[i] != value:
    arr[v] = arr[i]
    v+=1
print(arr[:v])