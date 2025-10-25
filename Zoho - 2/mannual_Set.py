def manual_set(arr):
  unique =[]
  for i in arr:
    if i not in unique:
      unique.append(i)
  return unique

arr = [1, 2, 2, 3, 4, 4, 5, 1]
unique_elements = manual_set(arr)
print("Unique Elements:", unique_elements)