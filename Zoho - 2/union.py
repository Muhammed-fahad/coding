def union(arr1,arr2):
  for num in arr1:
    if num in arr2:
      print(num)

arr1 = list(map(int,input("Enter a array 1: ").split()))
arr2 = list(map(int,input("Enter a array 2: ").split()))
print(union(arr1,arr2))