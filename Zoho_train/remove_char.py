s1 = "occurrence"
s2 = "car"

a = {}
for i in s1:
  if i in a:
    a[i] += 1
  else:
    a[i] = 1

for i in s2:
  if i in a:
    a[i] = 0

for i,j in a.items():
  if j:
    print(i,end="")

# print(a)
  