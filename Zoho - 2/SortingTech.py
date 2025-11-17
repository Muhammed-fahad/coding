value = str(input())
value_store = {}
for i in value:
  if i in value_store:
    value_store[i] += 1
  else:
    value_store[i] = 1

print(value_store)

# alphabetic assending order
ass = sorted(value_store.items())
print("Alphabetic" , ass)

# alpahebtic decending
alp_dec = sorted(value_store.items() , reverse=True)

print("alp_decending" , alp_dec)

# Accending 
Acc = dict(sorted(value_store.items() , key=lambda x:x[1]))
print("Accending order: " , Acc)

# decending
dec = dict(sorted(value_store.items(), key=lambda x: x[1] , reverse=True))
print("Decending order" , dec)