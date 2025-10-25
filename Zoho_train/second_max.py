arr = [16,17,4,3,18,5,2]
firstMax = -1
secondMax = -1

for i in arr:
  if i > firstMax:
    secondMax = firstMax
    firstMax = i
  
  else:
    if i > secondMax:
      secondMax = i

print(secondMax)
  