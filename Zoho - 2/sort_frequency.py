val = list(map(int,input("Enter the numbers: ").split()))
a = {}
for i in val:
  if i in a:
    a[i]+=1
  else:
    a[i] = 1

acc = dict(sorted(a.items(),key=lambda item:item[1] , reverse=True))
b = []
for key,val in acc.items():
  for i in range(val):
    b.append(key)
print(b)