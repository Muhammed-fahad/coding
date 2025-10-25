s = "aaabbccccd"
a = {}
for i in range(len(s)):
  if s[i] in a :
    a[s[i]] += 1
  else:
    a[s[i]] = 1

for i,j in a.items():
  print(i+str(j), end="")