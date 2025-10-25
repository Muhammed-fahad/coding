value = input("Enter the string : ").split()
for i in value:
  if(i == i[::-1] or len(i)== 1):
    value.remove(i)
print(" ".join(value))