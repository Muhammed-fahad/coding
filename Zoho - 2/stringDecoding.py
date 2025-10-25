def length(val):
  v=0
  for _ in val:
    v+=1
  return v

val = input("Enter String :")
store = ""
for i in range(0,length(val)-1,2):
  if(val[i+1]):
    store += val[i] * (ord(val[i+1])-48)
print(store)