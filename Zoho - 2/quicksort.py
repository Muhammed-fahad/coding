def quick_sort(arr):
  if len(arr)<=1:
    return arr
  pivot = arr[len(arr)//2]
  left = [i for i in arr if pivot > i]
  mid = [i for i in arr if pivot == i]
  right = [i for i in arr if pivot < i]
  
  return quick_sort(left) + mid + quick_sort(right)


arr = list(map(int,input("Enter the values to sort: ").split()))
print(quick_sort(arr))
