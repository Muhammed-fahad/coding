arr = [16,17,4,3,5,2]
max = -1
last = []

for i in range(len(arr)-1 , -1 , -1):
  if arr[i] > max:
    max = arr[i]
    last.append(max)
print(last[::-1])