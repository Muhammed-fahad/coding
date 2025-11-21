a = input("Enter a Number: ")
b = input("Enter a Number: ")

found = -1
for i in range(len(a) - len(b)+1 ): 
    if a[i:i+len(b)] == b:
        found = i+1
        break 
print(found)
