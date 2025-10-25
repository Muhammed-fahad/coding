value = input("Enter a String: ")
store = {}
for i in value:
  if i in store:
    store[i] += 1
  else:
    store[i] = 1

flage = True

for key,value in store.items():
  if value == 1:
    print(key)
    flage = False
    break
  
if flage:
  print("-1")
  