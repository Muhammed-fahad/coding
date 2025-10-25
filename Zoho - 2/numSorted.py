arr = [3,4,5,1,2]
flage = True
sort = sorted(arr)

for _ in range(len(arr)):
  if arr == sort:
    print("True")
    flage = False
    break
  arr = arr[1:]+[arr[0]]
if(flage):
  print("No it is not sorted")
