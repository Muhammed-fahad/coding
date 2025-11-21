from collections import Counter
val = input("Enter a string: ")
# store = Counter(val)
store = {}
for i in val:
  store[i] = store.get(i, 0) + 1
    
a = ""
for key,val in store.items():
  a = a+key+str(val)

print (a)