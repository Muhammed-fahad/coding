from collections import Counter
val = input("Enter a string: ")
# store = Counter(val)
store = {}
for i in val:
  if i in store:
    store[i] += 1
  else:
    store[i] = 1
    
a = ""
for key,val in store.items():
  a = a+key+str(val)

print (a)